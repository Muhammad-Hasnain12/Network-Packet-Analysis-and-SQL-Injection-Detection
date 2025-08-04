import joblib
import os
from analyze_pcap import extract_features

def test_model():
    """Test the trained model with sample payloads"""
    try:
        # Check if model exists
        if not os.path.exists('sql_injection_model.pkl'):
            print("Error: Model file 'sql_injection_model.pkl' not found")
            print("Please run train_model.py first to create the model")
            return
        
        # Load the model
        model = joblib.load('sql_injection_model.pkl')
        print("Model loaded successfully!")
        print(f"Model type: {type(model).__name__}")
        
        # Test payloads
        test_payloads = [
            "GET /index.html HTTP/1.1",  # Benign
            "GET /search?query=' OR '1'='1 -- HTTP/1.1",  # Malicious
            "GET /api/users HTTP/1.1",  # Benign
            "admin' OR '1'='1' --",  # Malicious
            "GET /search?q=normal HTTP/1.1",  # Benign
            "1' UNION SELECT username,password FROM users --",  # Malicious
        ]
        
        print("\nTesting model with sample payloads:")
        print("-" * 50)
        
        for payload in test_payloads:
            try:
                features = extract_features(payload)
                features_list = list(features.values())
                prediction = model.predict([features_list])[0]
                probability = model.predict_proba([features_list])[0]
                
                result = "MALICIOUS" if prediction == 1 else "BENIGN"
                confidence = max(probability) * 100
                
                print(f"Payload: {payload[:50]}...")
                print(f"Prediction: {result} (confidence: {confidence:.1f}%)")
                print(f"Features: {features}")
                print("-" * 50)
                
            except Exception as e:
                print(f"Error testing payload '{payload}': {e}")
                print("-" * 50)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_model()
