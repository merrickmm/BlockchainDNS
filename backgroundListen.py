from dnsChain import *
import socket
import time

def acceptData(s):
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
    return (data)

while True:
    try:
        testBlock = dnsChain()
        testBlock.chainRead()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('', 7024))
            data, addr = s.recvfrom(1024)
            data2 = data.decode('utf-8')
            info = data2.split()
        time.sleep(2)
        if info[1] == "U":
            cLen = testBlock.getSize()
            sendIP = info[0]
            time.sleep(2)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((sendIP, 7023))
                    pushLen = str(sendIP) + " " + str(cLen)
                    s.send(pushLen.encode('utf-8'))
        elif info[1] == "F":
            continue
        else:
            sendIP = info[0]
            time.sleep(2)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((sendIP, 7023))
                    pushLen = str(IPAddr) + " " + str(cLen)
                    s.send(pushLen.encode('utf-8'))
            
    except:
        time.sleep(5)
        pass
        
        
        
            
        
