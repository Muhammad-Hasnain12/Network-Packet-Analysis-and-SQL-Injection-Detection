import joblib

try:
    model = joblib.load('sql_injection_model.pkl')
    print("Model loaded successfully!")
    print(f"Model details: {model}")
except Exception as e:
    print(f"Failed to load model: {e}")
