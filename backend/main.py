import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

from ml.threat_detector import ThreatDetector

app = FastAPI(title="Insider Threat Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

detector = ThreatDetector()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'user_activity_logs.csv')

try:
    df_logs = pd.read_csv(DATA_PATH)
    # Ensure datetime format for nice reporting
    df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])
except:
    df_logs = pd.DataFrame()

class ActivityIncident(BaseModel):
    action: str
    department_accessed: str
    file_size_mb: float
    location: str
    device: str
    hour: int
    is_night: bool
    success: bool
    user: str = "unknown"

@app.get("/api/stats")
def get_stats():
    """Return high level dashboard statistics"""
    if df_logs.empty:
         return {"error": "Data not available"}
         
    total_activities = len(df_logs)
    anomalies = int(df_logs['is_anomaly'].sum())
    anomaly_rate = round((anomalies / total_activities) * 100, 2)
    users_count = int(df_logs['user'].nunique())
    
    # Recent activity
    recent = df_logs.sort_values(by='timestamp', ascending=False).head(15)
    recent['timestamp'] = recent['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")
    recent_activities = recent.to_dict(orient="records")
    
    # Anomalies specifically
    anomalies_df = df_logs[df_logs['is_anomaly'] == True].sort_values(by='timestamp', ascending=False).head(10)
    anomalies_df['timestamp'] = anomalies_df['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")
    recent_anomalies = anomalies_df.to_dict(orient="records")
    
    # Department breakdown of anomalies
    anomalies_by_dept = df_logs[df_logs['is_anomaly'] == True]['department_accessed'].value_counts().to_dict()
    
    # Timeline data for chart (Count of anomalies per day)
    df_logs['date'] = df_logs['timestamp'].dt.date
    daily_anomalies = df_logs[df_logs['is_anomaly'] == True].groupby('date').size()
    timeline_labels = [str(date) for date in daily_anomalies.index]
    timeline_data = daily_anomalies.values.tolist()

    return {
        "metrics": {
            "total_activities": total_activities,
            "total_anomalies": anomalies,
            "anomaly_rate": anomaly_rate,
            "monitored_users": users_count
        },
        "recent_activities": recent_activities,
        "recent_anomalies": recent_anomalies,
        "chart_data": {
            "department_labels": list(anomalies_by_dept.keys()),
            "department_data": list(anomalies_by_dept.values()),
            "timeline_labels": timeline_labels,
            "timeline_data": timeline_data
        }
    }

@app.post("/api/predict")
def predict_threat(activity: ActivityIncident):
    """Predict if a given activity is an insider threat"""
    data = activity.dict()
    result = detector.predict(data)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

# Serve Frontend static files if they exist
frontend_dir = os.path.join(BASE_DIR, 'frontend')
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_dashboard():
    index_path = os.path.join(BASE_DIR, 'frontend', 'index.html')
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "API is running. Frontend not found yet."}
