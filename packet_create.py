from scapy.all import *
import os

def create_http_packet(dst_ip, dst_port, sql_payload):
    """
    Creates a valid HTTP GET request packet with an SQL injection payload.
    """
    try:
        http_request = (
            f"GET /search?query={sql_payload} HTTP/1.1\r\n"
            f"Host: {dst_ip}\r\n"
            f"User-Agent: Scapy-Test\r\n"
            f"Accept: */*\r\n"
            f"\r\n"
        )
        packet = IP(dst=dst_ip) / TCP(dport=dst_port, sport=RandShort(), flags="PA") / http_request
        return packet
    except Exception as e:
        print(f"Error creating packet: {e}")
        return None

def main():
    """Main function to create test packets"""
    try:
        # Destination details
        dst_ip = "127.0.0.1"
        dst_port = 80
        sql_payload = "' OR '1'='1 --"
        
        print(f"Creating HTTP packet with SQL injection payload...")
        packet = create_http_packet(dst_ip, dst_port, sql_payload)
        
        if packet:
            output_pcap = "test_with_sql.pcap"
            wrpcap(output_pcap, [packet])
            print(f"Packet with SQL payload saved to {output_pcap}")
            
            # Verify file was created
            if os.path.exists(output_pcap):
                print(f"File created successfully: {os.path.getsize(output_pcap)} bytes")
            else:
                print("Error: File was not created")
        else:
            print("Error: Failed to create packet")
            
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
