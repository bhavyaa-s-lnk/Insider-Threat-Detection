import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'user_activity_logs.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'ml')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'encoders.pkl')

def load_and_preprocess_data():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH)
    
    # We will use simple feature engineering
    # Features: action, department_accessed, file_size_mb, location, device, hour, is_night, success
    features = ['action', 'department_accessed', 'file_size_mb', 'location', 'device', 'hour', 'is_night', 'success']
    X = df[features].copy()
    y = df['is_anomaly']

    # Encode categorical variables
    categorical_cols = ['action', 'department_accessed', 'location', 'device']
    encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le
        
    return X, y, encoders

def train_and_save():
    os.makedirs(MODEL_DIR, exist_ok=True)
    X, y, encoders = load_and_preprocess_data()
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    print(f"Saving model to {MODEL_PATH}...")
    joblib.dump(model, MODEL_PATH)
    joblib.dump(encoders, ENCODER_PATH)
    print("Done!")

if __name__ == "__main__":
    train_and_save()
