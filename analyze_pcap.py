import pyshark
import joblib
import pandas as pd

def extract_features(payload):
    print(f"Extracting features for payload: {payload}")
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
    print(f"Extracted features: {features}")
    return features

def extract_http_payloads(pcap_file):
    print(f"Reading HTTP payloads from {pcap_file}...")
    cap = pyshark.FileCapture(pcap_file, display_filter="http")
    payloads = []
    for packet in cap:
        try:
            # Log all HTTP fields to debug extraction
            print(f"Packet Info: {packet}")
            if hasattr(packet.http, 'request_full_uri'):
                print(f"Extracted request_full_uri: {packet.http.request_full_uri}")
                payloads.append(packet.http.request_full_uri)
            elif hasattr(packet.http, 'request_uri') and hasattr(packet.http, 'host'):
                uri = f"http://{packet.http.host}{packet.http.request_uri}"
                print(f"Constructed URI: {uri}")
                payloads.append(uri)
            else:
                print(f"No valid HTTP payload found in packet: {packet}")
        except AttributeError as e:
            print(f"Error processing packet: {e}")
    cap.close()
    print(f"Extracted HTTP payloads: {payloads}")
    return payloads

def analyze_pcap_with_model(pcap_file, model_file):
    print(f"Loading model from {model_file}...")
    model = joblib.load(model_file)
    print("Model loaded successfully.")

    http_payloads = extract_http_payloads(pcap_file)
    if not http_payloads:
        print("No HTTP payloads found in the pcap file.")
        return []

    print("Analyzing payloads for SQL injection...")
    results = []
    for payload in http_payloads:
        try:
            print(f"Analyzing payload: {payload}")
            features = extract_features(payload)
            print(f"Extracted features: {features}")
            # Convert features (dict) to list of values
            features_list = list(features.values())
            prediction = model.predict([features_list])[0]
            print(f"Prediction: {prediction}")
            results.append({'payload': payload, 'is_sqli': prediction})
        except Exception as e:
            print(f"Error analyzing payload: {payload}. Error: {e}")
    print(f"Analysis completed. {len(results)} payloads analyzed.")
    return results

def generate_report(results, output_file):
    if not results:
        print("No results to save. Adding placeholder.")
        results = [{'payload': 'No data found', 'is_sqli': None}]
    
    # Log all results for debugging
    for result in results:
        print(f"Saving result: {result}")

    # Write results to CSV
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Report saved to {output_file}")

# Analyze
pcap_file = "edited_test_with_sql.pcap"
model_file = "sql_injection_model.pkl"
results = analyze_pcap_with_model(pcap_file, model_file)
generate_report(results, "sql_injection_report.csv")
