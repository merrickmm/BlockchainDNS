from dnsChain import *
import socket
import time


#sets personal hostname and IP
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
IPlist = IPAddr.split('.')
network = str(IPlist[0]) + "." + str(IPlist[1]) + "." + str(IPlist[2]) + "."

#imports chain from CSV or creates genesis if not found
try:
    testBlock = dnsChain()
    testBlock.chainRead()
    
except:
    testBlock = dnsChain()

#Function to accept data over TCP
def acceptData(s):
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
    return (data)

#Sends broadcast for update response, handles response
def update(block, IPAddr, hostname, network):
    #Broadcasts for update
    for i in range(1,255):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s3:
            pushUpdate = str(IPAddr) + " " + "U"
            pushIP = network + str(i)
            if pushIP == IPAddr:
                pass
            else:
                s3.sendto(pushUpdate.encode('utf-8'),(pushIP, 7024))
        
    #Listens for update response takes (ip, len)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            s2.settimeout(5)
            s2.bind(('', 7023))
            s2.listen()
            data = acceptData(s2)
            data2 = data.decode('utf-8')
            info = data2.split()
            upIP = info[0]
            upLen = info[1]

        #continues to take updates until sizes of chains match
        while True:
            cLen = block.getSize()
            time.sleep(2)
            if upLen <= cLen:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((upIP, 7024))
                    pushLen = str(IPAddr) + " " + "F"
                    s.send(pushLen.encode('utf-8'))
                continue
            else:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((upIP, 7024))
                    pushLen = str(IPAddr) + " " + str(cLen)
                    s.send(pushLen.encode('utf-8'))
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind((upIP, 7023))
                    s.listen()
                    data = acceptData(s)
                    data2 = data.decode('utf-8')
                    info = data2.split()

                    block.addBlock("test", "test")

                    block.blocks[cLen].index = info[0]
                    
                    dat1 = info[1]
                    dat2 = info[2]
                    block.blocks[cLen].timestamp = dat1 + " " + dat2

                    block.blocks[cLen].host = info[3]

                    block.blocks[cLen].ip = info[4]

                    block.blocks[cLen].pHash = info[5]

                    block.blocks[cLen].cHash = info[6]

    #If no connection is found checks to add self                
    except:
        cLen = block.getSize()
        self = False
        for i in range(0,cLen + 1):
            if block.blocks[i].ip == IPAddr:
                self = True
            else:
                pass
        print(self)

        if self:
            pass
        else:
            block.addBlock(hostname, IPAddr)
    return(block)

#Continues to loop every 30 seconds
while True:
    testBlock = update(testBlock, IPAddr, hostname, network)
    wLen = testBlock.getSize()
    testBlock.chainWrite(wLen + 1)
    time.sleep(30)
    
        
