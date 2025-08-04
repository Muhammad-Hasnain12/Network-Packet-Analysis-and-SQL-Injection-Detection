from scapy.all import *
import os

def edit_pcap_file(input_pcap, output_pcap):
    """
    Edit PCAP file to modify HTTP payloads with SQL injection
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_pcap):
            print(f"Error: Input file {input_pcap} not found")
            return False
        
        # Load the original .pcap file
        print(f"Loading packets from {input_pcap}...")
        packets = rdpcap(input_pcap)
        print(f"Loaded {len(packets)} packets")
        
        modified_count = 0
        
        # Edit the HTTP payload of packets
        for i, packet in enumerate(packets):
            if packet.haslayer(Raw):  # Check if the packet has a payload
                try:
                    raw_data = packet[Raw].load.decode(errors='ignore')  # Decode the payload
                    
                    # Modify the payload (example: add or fix SQL injection string)
                    if "GET" in raw_data and "/search?query=" in raw_data:
                        modified_data = raw_data.replace("/search?query=", "/search?query=' OR '1'='1 --")
                        packet[Raw].load = modified_data.encode()  # Update the payload
                        modified_count += 1
                        
                        # Recalculate lengths and checksums
                        if packet.haslayer(IP):
                            del packet[IP].len
                            del packet[IP].chksum
                        if packet.haslayer(TCP):
                            del packet[TCP].chksum
                            
                except Exception as e:
                    print(f"Error processing packet {i}: {e}")
                    continue
        
        # Save the modified packets to a new .pcap file
        wrpcap(output_pcap, packets)
        print(f"Modified {modified_count} packets")
        print(f"Modified .pcap saved as {output_pcap}")
        
        # Verify output file
        if os.path.exists(output_pcap):
            print(f"Output file created successfully: {os.path.getsize(output_pcap)} bytes")
            return True
        else:
            print("Error: Output file was not created")
            return False
            
    except Exception as e:
        print(f"Error editing PCAP file: {e}")
        return False

def main():
    """Main function to edit PCAP file"""
    input_pcap = "test_with_sql.pcap"
    output_pcap = "edited_test_with_sql.pcap"
    
    success = edit_pcap_file(input_pcap, output_pcap)
    if success:
        print("PCAP editing completed successfully")
    else:
        print("PCAP editing failed")

if __name__ == "__main__":
    main()
