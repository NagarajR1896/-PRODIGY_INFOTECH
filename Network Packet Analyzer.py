from scapy.all import sniff, TCP, UDP, ICMP, DNS, IP, wrpcap

res = []

def packet_callback(packet):
    if packet.haslayer(IP):  
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if packet.haslayer(TTCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            if src_port == 80 or dst_port == 80:
                print(f"[HTTP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            else:
                print(f"[TCP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"[UDP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            if packet.haslayer(DNS) and packet[DNS].qd:
                dns_query = packet[DNS].qd.qname.decode('utf-8')
                print(f"[DNS Query] {dns_query}")

        elif packet.haslayer(ICMP):
            print(f"[ICMP] {src_ip} -> {dst_ip}")

        res.append(packet)

if __name__ == "__main__":
    print("Starting packet capture...")
    try:
        sniff(prn=packet_callback, count=0)  
    except KeyboardInterrupt:
        print("Packet capture interrupted.")
    finally:
        pcap_filename = "res.pcap"
        wrpcap(pcap_filename, res)
        print(f"Packets saved to {pcap_filename}")
