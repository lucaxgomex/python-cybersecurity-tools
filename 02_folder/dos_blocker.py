import os, sys, time
from collections import defaultdict
from scapy import sniff, IP # type: ignore

THRESHOLD = 40

print(f'THRESHOLD: {THRESHOLD}')

def package_callback(package):
    scr_ip = package[IP].src
    packet_count[scr_ip] += 1
    current_time = time.time()
    time_interval = current_time - start_time[0]

    if time_interval >= 1:
        for ip, count int pack