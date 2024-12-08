from scapy.all import *

def create_http_packet(dst_ip, dst_port, sql_payload):
    """
    Creates a valid HTTP GET request packet with an SQL injection payload.
    """
    http_request = (
        f"GET /search?query={sql_payload} HTTP/1.1\r\n"
        f"Host: {dst_ip}\r\n"
        f"User-Agent: Scapy-Test\r\n"
        f"Accept: */*\r\n"
        f"\r\n"
    )
    print(f"Full HTTP Request:\n{http_request}")  # Debugging
    packet = IP(dst=dst_ip) / TCP(dport=dst_port, sport=RandShort(), flags="PA") / http_request
    return packet

# Destination details
dst_ip = "127.0.0.1"
dst_port = 80
sql_payload = "' OR '1'='1 --"

packet = create_http_packet(dst_ip, dst_port, sql_payload)
output_pcap = "test_with_sql.pcap"
wrpcap(output_pcap, [packet])
print(f"Packet with SQL payload saved to {output_pcap}")
