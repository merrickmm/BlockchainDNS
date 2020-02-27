from dnsChain import *
import socket

def testPush():
    pushBlock = dnsChain()
    pushBlock.addBlock("192.168.1.1")
    pushBlock.addBlock("192.168.1.2")
    
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 7023         # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(pushBlock)
        data = s.recv(1024)
testPush()    
