# Python script to debug transfers using SOS
# cat /proc/meminfo
# cat /proc/loadavg

import dpkt
import socket

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    if socket.inet_ntoa(ip.src) == "10.0.0.3":
        print(tcp.win)
