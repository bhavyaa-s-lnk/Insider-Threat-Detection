// Configure Chart.js global defaults for dark theme
Chart.defaults.color = '#94a3b8';
Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';

document.addEventListener('DOMContentLoaded', () => {
    fetchDashboardData();
    // Poll every 10 seconds
    setInterval(fetchDashboardData, 10000);
});

async function fetchDashboardData() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        if (data.error) {
            console.error("API Error:", data.error);
            return;
        }

        updateMetrics(data.metrics);
        updateTables(data.recent_activities, data.recent_anomalies);
        renderCharts(data.chart_data);
    } catch (error) {
        console.error("Failed to fetch dashboard data:", error);
    }
}

function updateMetrics(metrics) {
    document.getElementById('val-total').textContent = metrics.total_activities.toLocaleString();
    document.getElementById('val-users').textContent = metrics.monitored_users;
    document.getElementById('val-anomalies').textContent = metrics.total_anomalies.toLocaleString();
    document.getElementById('val-rate').textContent = `${metrics.anomaly_rate}%`;
}

function updateTables(activities, anomalies) {
    // Populate Activity Table
    const activityTbody = document.querySelector('#activityTable tbody');
    activityTbody.innerHTML = '';
    
    activities.forEach(act => {
        const tr = document.createElement('tr');
        const statusClass = act.is_anomaly ? 'text-danger' : 'text-success';
        const statusText = act.is_anomaly ? 'Suspicious' : 'Normal';
        
        tr.innerHTML = `
            <td>${act.timestamp.split(' ')[1]}</td>
            <td>${act.user}</td>
            <td>${act.action}</td>
            <td class="${statusClass}">${statusText}</td>
        `;
        activityTbody.appendChild(tr);
    });

    // Populate Anomalies Table
    const anomalyTbody = document.querySelector('#anomaliesTable tbody');
    anomalyTbody.innerHTML = '';
    
    anomalies.forEach(anom => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${anom.timestamp.split(' ')[1]}</td>
            <td class="text-danger">${anom.user}</td>
            <td>${anom.action} <br><small>${anom.file_size_mb > 0 ? anom.file_size_mb + 'MB' : ''}</small></td>
            <td>${anom.location}</td>
        `;
        anomalyTbody.appendChild(tr);
    });
}

let timelineChartInstance = null;
let deptChartInstance = null;

function renderCharts(chartData) {
    // Timeline Chart
    const ctxTimeline = document.getElementById('timelineChart').getContext('2d');
    
    if (timelineChartInstance) timelineChartInstance.destroy();
    
    timelineChartInstance = new Chart(ctxTimeline, {
        type: 'line',
        data: {
            labels: chartData.timeline_labels,
            datasets: [{
                label: 'Anomalies Detected',
                data: chartData.timeline_data,
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Department Chart
    const ctxDept = document.getElementById('deptChart').getContext('2d');
    
    if (deptChartInstance) deptChartInstance.destroy();
    
    deptChartInstance = new Chart(ctxDept, {
        type: 'doughnut',
        data: {
            labels: chartData.department_labels,
            datasets: [{
                data: chartData.department_data,
                backgroundColor: [
                    '#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'right' },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return ' ' + context.formattedValue + ' Anomalies';
                        }
                    }
                }
            },
            cutout: '70%'
        }
    });
}
