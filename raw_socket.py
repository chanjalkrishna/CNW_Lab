import socket
import struct

# Create raw socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Packet Capturing Started...")
print("Waiting for packets...\n")

try:
    while True:

        # Capture packet
        packet, addr = s.recvfrom(65565)

        # Extract Ethernet header
        eth_header = packet[:14]

        eth = struct.unpack('!6s6sH', eth_header)

        protocol = eth[2]

        # Check for IPv4 packet
        if protocol == 0x0800:

            # Extract IP header
            ip_header = packet[14:34]

            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            # Extract source and destination IP
            source_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])

            # Extract protocol number
            proto = iph[6]

            if proto == 1:
                protocol_name = "ICMP"

            elif proto == 6:
                protocol_name = "TCP"

            elif proto == 17:
                protocol_name = "UDP"

            else:
                protocol_name = "Other"

            print("Source IP:", source_ip)
            print("Destination IP:", dest_ip)
            print("Protocol:", protocol_name)
            print("--------------------------")

except KeyboardInterrupt:
    print("\nPacket Capturing Stopped")

finally:
    s.close()
