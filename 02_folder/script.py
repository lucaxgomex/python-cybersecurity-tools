import sys
import time
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from scapy.all import sendp

TARGET_IP = '192.168.x.x'
INTERFACE = 'eth0'
NUM_PACKETS = 100
DURATION = 5

def send_packets(target_ip, interface, num_packets, duration):
    packet = Ether() / IP(kargs = target_ip) / TCP()
    end_time = time.time() + duration
    packet_count = 0

    while (time.time() < end_time) and (packet_count < num_packets):
        sendp(packet, iface = interface)
        packet_count += 1

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('This script requires Python 3.0+')
        sys.exit(1)
    
    send_packets(
        TARGET_IP,
        INTERFACE,
        NUM_PACKETS,
        DURATION
    )