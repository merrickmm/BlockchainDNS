from dnsChain import *
import socket
import time

pushBlock = dnsChain()
pushBlock.addBlock("192.168.1.1")
pushBlock.addBlock("192.168.1.2")

space = " "
            
def testPush():    
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 7023         # The port used by the server
    length = pushBlock.getSize() + 1
    print (length)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(0, length):
            index = str(pushBlock.blocks[i].index)
            timestamp = str(pushBlock.blocks[i].timestamp)
            ip = str(pushBlock.blocks[i].ip)
            pHash = str(pushBlock.blocks[i].pHash)
            cHash = str(pushBlock.blocks[i].cHash)

            s.send(index.encode('utf-8'))
            s.send(space.encode('utf-8'))
            s.send(timestamp.encode('utf-8'))
            s.send(space.encode('utf-8'))
            s.send(ip.encode('utf-8'))
            s.send(space.encode('utf-8'))
            s.send(pHash.encode('utf-8'))
            s.send(space.encode('utf-8'))
            s.send(cHash.encode('utf-8'))
            s.send(space.encode('utf-8'))

            

testPush()
