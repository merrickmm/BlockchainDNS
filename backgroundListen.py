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
    #try:
        testBlock = dnsChain()
        testBlock.chainRead()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('', 7024))
            data, addr = s.recvfrom(1024)
            data2 = data.decode('utf-8')
            info = data2.split()
        time.sleep(2)
        if info[1] == "U":
            print("hit")
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
                    space = " "
                    pushIndex = str(testBlock.blocks[i].index)
                    pushTimestamp = str(testBlock.blocks[i].timestamp)
                    pushHost = str(testBlock.blocks[i].host)
                    pushIp = str(testBlock.blocks[i].ip)
                    pushPHash = str(testBlock.blocks[i].pHash)
                    pushCHash = str(testBlock.blocks[i].cHash)

                    s.send(pushIndex.encode('utf-8'))
                    s.send(space.encode('utf-8'))
                    s.send(pushTimestamp.encode('utf-8'))
                    s.send(space.encode('utf-8'))
                    s.send(pushHost.encode('utf-8'))
                    s.send(space.encode('utf-8'))
                    s.send(pushIp.encode('utf-8'))
                    s.send(space.encode('utf-8'))
                    s.send(pushPHash.encode('utf-8'))
                    s.send(space.encode('utf-8'))
                    s.send(pushCHash.encode('utf-8'))
            
    #except:
        #time.sleep(5)
        #pass
        
        
        
            
        
