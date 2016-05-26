# Python script to debug transfers using SOS
# cat /proc/meminfo
# cat /proc/loadavg

import dpkt
import socket

import plotly.plotly as py
import plotly.graph_objs as go

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)

windows = []
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    if socket.inet_ntoa(ip.src) == "10.0.0.3":
        windows.append(tcp.win)
        #print(tcp.win)

print windows

