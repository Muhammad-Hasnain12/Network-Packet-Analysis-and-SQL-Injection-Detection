from scapy.all import *

# Load the original .pcap file
input_pcap = "test_with_sql.pcap"  # Replace with your .pcap file name
output_pcap = "edited_test_with_sql.pcap"

packets = rdpcap(input_pcap)

# Edit the HTTP payload of the desired packet (e.g., the first HTTP packet)
for packet in packets:
    if packet.haslayer(Raw):  # Check if the packet has a payload
        raw_data = packet[Raw].load.decode(errors='ignore')  # Decode the payload
        print(f"Original Payload: {raw_data}")

        # Modify the payload (example: add or fix SQL injection string)
        if "GET" in raw_data:
            modified_data = raw_data.replace("/search?query=", "/search?query=' OR '1'='1 --")
            print(f"Modified Payload: {modified_data}")
            packet[Raw].load = modified_data.encode()  # Update the payload

        # Recalculate lengths and checksums
        del packet[IP].len
        del packet[IP].chksum
        del packet[TCP].chksum

# Save the modified packets to a new .pcap file
wrpcap(output_pcap, packets)
print(f"Modified .pcap saved as {output_pcap}")
