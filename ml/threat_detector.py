import joblib
import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'ml')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'encoders.pkl')

class ThreatDetector:
    def __init__(self):
        self.model = None
        self.encoders = None
        self._load_model()
        
    def _load_model(self):
        if os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
            self.model = joblib.load(MODEL_PATH)
            self.encoders = joblib.load(ENCODER_PATH)
        else:
            print("Model files not found. Please train the model first.")
            
    def predict(self, activity_data: dict) -> dict:
        """
        Predict if an activity is anomalous.
        Returns a dict with prediction and anomaly probability.
        """
        if not self.model or not self.encoders:
            return {"error": "Model not loaded properly."}
            
        try:
            # Prepare dataframe
            df = pd.DataFrame([activity_data])
            features = ['action', 'department_accessed', 'file_size_mb', 'location', 'device', 'hour', 'is_night', 'success']
            X = df[features].copy()
            
            # Encode categorical features
            categorical_cols = ['action', 'department_accessed', 'location', 'device']
            for col in categorical_cols:
                if col in self.encoders:
                    # Map standard labels or map to -1 for unknown
                    classes = self.encoders[col].classes_
                    X[col] = X[col].apply(lambda x: self.encoders[col].transform([x])[0] if x in classes else -1)

            # Predict
            is_anomaly = bool(self.model.predict(X)[0])
            prob = float(self.model.predict_proba(X)[0][1])
            
            return {
                "is_anomaly": is_anomaly,
                "threat_score": min(round(prob * 100), 100)
            }
        except Exception as e:
            return {"error": str(e)}
