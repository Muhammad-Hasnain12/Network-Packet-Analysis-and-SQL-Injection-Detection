import pyshark
import joblib
import pandas as pd
import os

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

def extract_http_payloads(pcap_file):
    """Extract HTTP payloads from PCAP file"""
    if not os.path.exists(pcap_file):
        print(f"Error: PCAP file {pcap_file} not found")
        return []
    
    try:
        cap = pyshark.FileCapture(pcap_file, display_filter="http")
        payloads = []
        
        for packet in cap:
            try:
                if hasattr(packet, 'http'):
                    if hasattr(packet.http, 'request_full_uri') and packet.http.request_full_uri:
                        payloads.append(packet.http.request_full_uri)
                    elif hasattr(packet.http, 'request_uri') and hasattr(packet.http, 'host'):
                        uri = f"http://{packet.http.host}{packet.http.request_uri}"
                        payloads.append(uri)
                    elif hasattr(packet.http, 'request_uri'):
                        payloads.append(packet.http.request_uri)
            except (AttributeError, Exception) as e:
                continue  # Skip problematic packets
                
        cap.close()
        return payloads
    except Exception as e:
        print(f"Error reading PCAP file: {e}")
        return []

def analyze_pcap_with_model(pcap_file, model_file):
    """Analyze PCAP file using trained model"""
    if not os.path.exists(model_file):
        print(f"Error: Model file {model_file} not found")
        return []
    
    try:
        model = joblib.load(model_file)
    except Exception as e:
        print(f"Error loading model: {e}")
        return []

    http_payloads = extract_http_payloads(pcap_file)
    if not http_payloads:
        print("No HTTP payloads found in the pcap file.")
        return []

    results = []
    for payload in http_payloads:
        try:
            features = extract_features(payload)
            features_list = list(features.values())
            prediction = model.predict([features_list])[0]
            results.append({'payload': payload, 'is_sqli': prediction})
        except Exception as e:
            print(f"Error analyzing payload: {payload}. Error: {e}")
            continue
    
    print(f"Analysis completed. {len(results)} payloads analyzed.")
    return results

def generate_report(results, output_file):
    """Generate and save analysis report"""
    try:
        if not results:
            print("No results to save.")
            return False
        
        df = pd.DataFrame(results)
        df.to_csv(output_file, index=False)
        print(f"Report saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error saving report: {e}")
        return False

def main():
    """Main function to run the analysis"""
    pcap_file = "edited_test_with_sql.pcap"
    model_file = "sql_injection_model.pkl"
    
    if not os.path.exists(pcap_file):
        print(f"Error: PCAP file {pcap_file} not found")
        return
    
    if not os.path.exists(model_file):
        print(f"Error: Model file {model_file} not found")
        return
    
    results = analyze_pcap_with_model(pcap_file, model_file)
    if results:
        generate_report(results, "sql_injection_report.csv")
    else:
        print("No analysis results to report.")

if __name__ == "__main__":
    main()
