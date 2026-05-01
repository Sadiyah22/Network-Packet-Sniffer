from scapy.all import sniff

def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        
        print(f"[+] IP Packet: {src_ip} -> {dst_ip} | Protocol: {proto}")

print("[*] Starting packet sniffer... Press Ctrl+C to stop.")

# Capture packets and send them to our function
# Note: This usually requires 'sudo' on Mac/Linux or Admin on Windows
sniff(prn=process_packet, store=0)
