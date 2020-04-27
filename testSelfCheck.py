from dnsChain import *
import socket
import time

#sets personal hostname and IP
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
IPlist = IPAddr.split('.')
network = str(IPlist[0]) + "." + str(IPlist[1]) + "." + str(IPlist[2]) + "."

testBlock = dnsChain()

self = False
for i in range(0,1):
    if testBlock.blocks[i].ip == IPAddr:
        self = True
    else:
        pass
print(self)
