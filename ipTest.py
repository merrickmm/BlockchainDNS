import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
IPlist = IPAddr.split('.')
network = str(IPlist[0]) + "." + str(IPlist[1]) + "." + str(IPlist[2]) + "."
print(network) 
print(IPlist)
print(hostname)
print(IPAddr)
