import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Feature extraction function
def extract_features(payload):
    sql_keywords = [
        'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION',
        'EXEC', 'XP_', 'CHAR', 'CAST', 'CONVERT', 'LOAD_FILE', 
        'SLEEP', 'DATABASE', 'USER', 'VERSION'
    ]
    special_chars = ['\'', '"', ';', '--', '#', '/*', '*/']
    specific_patterns = [
        "' OR '1'='1", '" OR "1"="1', 'OR 1=1', 'AND 1=1', 'AND 1=0',
        "' UNION SELECT", '" UNION SELECT', '; DROP TABLE', 'WAITFOR DELAY',
        '0x', '--', '#', '/*'
    ]
    features = {
        'length': len(payload),
        'sql_keywords': sum(payload.upper().count(kw) for kw in sql_keywords),
        'special_chars': sum(payload.count(ch) for ch in special_chars),
        'specific_patterns': sum(1 for pattern in specific_patterns if pattern in payload),
    }
    return features

# Dataset
# Updated dataset
data = [
    {'payload': "' OR '1'='1 --", 'label': 1},  # Malicious
    {'payload': "' UNION SELECT username, password FROM users --", 'label': 1},  # Malicious
    {'payload': "'; DROP TABLE users; --", 'label': 1},  # Malicious
    {'payload': "SELECT * FROM users WHERE id=1", 'label': 1},  # Malicious
    {'payload': "GET /index.html HTTP/1.1", 'label': 0},  # Benign
    {'payload': "GET /home HTTP/1.1", 'label': 0},  # Benign
    {'payload': "GET /search?query=' OR '1'='1 -- HTTP/1.1", 'label': 1},  # Malicious
]
df = pd.DataFrame(data)

# Feature extraction
df_features = pd.DataFrame([extract_features(row['payload']) for _, row in df.iterrows()])
X = df_features
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'sql_injection_model.pkl')
print("Model saved as sql_injection_model.pkl")

# Evaluate the model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
