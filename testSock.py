from dnsChain import *
import socket
import time

pushBlock = dnsChain()
pushBlock.addBlock("192.168.1.1")
pushBlock.addBlock("192.168.1.2")

            
def testPush():    
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 7023         # The port used by the server
    length = pushBlock.getSize() + 1
    print (length)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(0, length):
            test = str(pushBlock.blocks[i].index)
            print (test)
            s.send(test.encode('utf-8'))
            data = s.recv(1024)
            time.sleep(2)

testPush()
