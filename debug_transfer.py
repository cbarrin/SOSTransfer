# Python script to debug transfers using SOS
# cat /proc/meminfo
# cat /proc/loadavg

import dpkt

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    print ip.src
    print tcp.win