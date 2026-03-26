# Insider Threat Detection System

A production-ready insider threat detection system equipped with a graphical user interface, built exclusively for analyzing user activity logs and anomaly detection patterns. This system integrates backend data processing, machine learning models to identify suspicious behavior, and an intuitive frontend dashboard to visualize threats.

## Features

- **Custom-built ML Pipeline**: Uses Isolation Forest to detect anomalies in user activity.
- **RESTful API Backend**: Built with FastAPI to serve predictions and dashboard statistics.
- **Interactive Dashboard**: A custom dark-mode, glassmorphism-inspired UI to monitor alerts, anomaly scores, and recent user activities.
- **Data Generation**: Includes scripts to generate synthetic user activity logs for training and testing.
- **Tutorial & Practice**: Contains practice exercises and data exploration scripts to understand the pipeline.

## Project Structure

- `backend/` - FastAPI backend server
- `frontend/` - HTML, CSS, and JS files for the interactive dashboard
- `ml/` - Machine learning training and prediction scripts
- `Tutorial/` - Educational scripts and data exploration tools
- `generate_sample_data.py` - Script to generate the synthetic `user_activity_logs.csv`
- `practice_exercises.py` - Python script containing ML practice exercises
- `requirements.txt` - Python dependencies needed to run the project
- `user_activity_logs.csv` - The generated dataset of user activities

## Setup Instructions

### Prerequisites
- Python 3.8+

### 1. Install Dependencies
Open your terminal and install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Generate Data (Optional)
If you need fresh data, run the data generation script:
```bash
python generate_sample_data.py
```

### 3. Train the Model
Train the machine learning model on the generated data:
```bash
python ml/train.py
```

### 4. Start the Backend Server
Start the FastAPI backend server (runs on `http://127.0.0.1:8000`):
```bash
uvicorn backend.main:app --reload
```
*Note: Make sure to run this from the root project directory so it can find the `backend` module.*

### 5. Open the Dashboard
To view the UI, simply open `frontend/index.html` in your web browser. 

For a better experience (to avoid CORS issues), you can serve the frontend directory using a simple HTTP server:
```bash
cd frontend
python -m http.server 3000
```
Then visit `http://127.0.0.1:3000` in your browser.

## Exclusivity
This project was designed and built from scratch securely and exclusively for its owner, featuring a custom-tailored dataset generation, machine learning logic, backend API, and a unique glassmorphism frontend dashboard.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
