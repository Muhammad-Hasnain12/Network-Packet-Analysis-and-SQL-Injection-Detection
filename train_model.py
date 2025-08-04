import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def extract_features(payload):
    """Extract features from payload for SQL injection detection"""
    if not payload or not isinstance(payload, str):
        return {
            'length': 0,
            'sql_keywords': 0,
            'special_chars': 0,
            'specific_patterns': 0,
        }
    
    sql_keywords = [
        'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION',
        'EXEC', 'XP_', 'CHAR', 'CAST', 'CONVERT', 'LOAD_FILE', 
        'SLEEP', 'DATABASE', 'USER', 'VERSION', 'INFORMATION_SCHEMA',
        'BENCHMARK', 'SLEEP', 'WAITFOR', 'DELAY', 'BENCHMARK'
    ]
    special_chars = ['\'', '"', ';', '--', '#', '/*', '*/', '=', '<', '>']
    specific_patterns = [
        "' OR '1'='1", '" OR "1"="1', 'OR 1=1', 'AND 1=1', 'AND 1=0',
        "' UNION SELECT", '" UNION SELECT', '; DROP TABLE', 'WAITFOR DELAY',
        '0x', '--', '#', '/*', 'UNION ALL', 'OR 1=1--', 'OR 1=1#',
        'OR 1=1/*', 'OR 1=1*/', 'OR 1=1 OR', 'OR 1=1 AND'
    ]
    
    payload_upper = payload.upper()
    features = {
        'length': len(payload),
        'sql_keywords': sum(payload_upper.count(kw) for kw in sql_keywords),
        'special_chars': sum(payload.count(ch) for ch in special_chars),
        'specific_patterns': sum(1 for pattern in specific_patterns if pattern.upper() in payload_upper),
    }
    return features

# Enhanced dataset with more examples
data = [
    # Malicious SQL injection examples
    {'payload': "' OR '1'='1 --", 'label': 1},
    {'payload': "' UNION SELECT username, password FROM users --", 'label': 1},
    {'payload': "'; DROP TABLE users; --", 'label': 1},
    {'payload': "SELECT * FROM users WHERE id=1", 'label': 1},
    {'payload': "GET /search?query=' OR '1'='1 -- HTTP/1.1", 'label': 1},
    {'payload': "admin' OR '1'='1' --", 'label': 1},
    {'payload': "1' UNION SELECT NULL,NULL,NULL--", 'label': 1},
    {'payload': "'; WAITFOR DELAY '00:00:05'--", 'label': 1},
    {'payload': "1' AND 1=1--", 'label': 1},
    {'payload': "1' AND 1=0--", 'label': 1},
    {'payload': "1' OR 1=1#", 'label': 1},
    {'payload': "1' OR 1=1/*", 'label': 1},
    {'payload': "1' UNION ALL SELECT NULL--", 'label': 1},
    {'payload': "1' AND SLEEP(5)--", 'label': 1},
    {'payload': "1' AND BENCHMARK(1000000,MD5(1))--", 'label': 1},
    {'payload': "1' AND (SELECT COUNT(*) FROM information_schema.tables)>0--", 'label': 1},
    
    # Benign examples
    {'payload': "GET /index.html HTTP/1.1", 'label': 0},
    {'payload': "GET /home HTTP/1.1", 'label': 0},
    {'payload': "GET /about HTTP/1.1", 'label': 0},
    {'payload': "GET /contact HTTP/1.1", 'label': 0},
    {'payload': "GET /products HTTP/1.1", 'label': 0},
    {'payload': "GET /search?query=normal HTTP/1.1", 'label': 0},
    {'payload': "GET /api/users HTTP/1.1", 'label': 0},
    {'payload': "POST /login HTTP/1.1", 'label': 0},
    {'payload': "GET /images/logo.png HTTP/1.1", 'label': 0},
    {'payload': "GET /css/style.css HTTP/1.1", 'label': 0},
    {'payload': "GET /js/app.js HTTP/1.1", 'label': 0},
    {'payload': "GET /api/data?limit=10 HTTP/1.1", 'label': 0},
    {'payload': "GET /search?q=test&page=1 HTTP/1.1", 'label': 0},
    {'payload': "GET /user/profile HTTP/1.1", 'label': 0},
    {'payload': "GET /admin/dashboard HTTP/1.1", 'label': 0},
]
df = pd.DataFrame(data)

def main():
    """Main function to train the model"""
    try:
        # Feature extraction
        print("Extracting features from dataset...")
        df_features = pd.DataFrame([extract_features(row['payload']) for _, row in df.iterrows()])
        X = df_features
        y = df['label']
        
        print(f"Dataset shape: {X.shape}")
        print(f"Features: {list(X.columns)}")
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        print(f"Training set size: {len(X_train)}")
        print(f"Test set size: {len(X_test)}")
        
        # Train model
        print("Training Random Forest model...")
        model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        model.fit(X_train, y_train)
        
        # Save the model
        joblib.dump(model, 'sql_injection_model.pkl')
        print("Model saved as sql_injection_model.pkl")
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nFeature Importance:")
        print(feature_importance)
        
    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    main()
