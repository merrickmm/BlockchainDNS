from dnsChain import *
import socket

recieved = "Recieved"
def acceptData(s):
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
    return (data)
                        
#sets while conditional to true
run = True

#start GUI loop and prints options
while run == True:
    print("Select one of the following options: ")
    print("\t[1] Create a new chain (Must be ran first)")
    print("\t[2] Add a block to a chain")
    print("\t[3] Print a chain")
    print("\t[4] Verify a chain")
    print("\t[5] Output to CSV")
    print("\t[6] Load chain from CSV")
    print("\t[7] Accepts chain from node")
    print("\t[8] Sends current chain")
    print("\t[E]xit")
    opt = input("")

    #Create chain option(must be ran first)
    if opt == "1":
        testBlock = dnsChain()
        
    #Adds block to chain with given IP
    elif opt == "2":
        inHost = input ("Enter the hostname: ")
        inIP = input("Enter the IP address: ")
        testBlock.addBlock(inHost, inIP)


    #Prints current block data of chain
    elif opt == "3":
        length = testBlock.getSize() + 1
        for i in range(0, length):
            print ("Index: ", testBlock.blocks[i].index)
            print (f"\tTimestamp: ", testBlock.blocks[i].timestamp)
            print (f"\tHost: ", testBlock.blocks[i].host)
            print (f"\tIP: ", testBlock.blocks[i].ip)
            print (f"\tPrevious Hash: ", testBlock.blocks[i].pHash)
            print (f"\tCurrent Hash: ", testBlock.blocks[i].cHash)
            print ("")

    #Verifies block data in chain
    elif opt == "4":
        testBlock.verify()

    #Outputs Chain to a CSV file
    elif opt == "5":
        length = testBlock.getSize()
        testBlock.chainWrite(length + 1)

    #Loads Chain from a CSV file
    elif opt == "6":
        testBlock = dnsChain()
        testBlock.chainRead()

    #Listens for chain update
    elif opt == "7":
        HOST = ''  
        PORT = 7023        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            data = acceptData(s)
            data2 = data.decode('utf-8')

            #Splits sent data and determines length in blocks
            info = data2.split()
            points = len(info)
            print (info)
            print (points)
            blockLen = int(points/7)
            print (blockLen)

            #Appednds to chain
            ind = 0
            for i in range(blockLen):
                try:
                    testBlock.blocks[i].index = info[ind]
                    ind = ind + 1
                    dat1 = info[ind]
                    ind = ind + 1
                    dat2 = info[ind]
                    testBlock.blocks[i].timestamp = dat1 + " " + dat2
                    ind = ind + 1
                    testBolck.blocks[i].host = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].ip = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].pHash = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].cHash = info[ind]
                    ind = ind + 1
                except:
                    testBlock.addBlock("test", "test")
                    testBlock.blocks[i].index = info[ind]
                    ind = ind + 1
                    dat1 = info[ind]
                    ind = ind + 1
                    dat2 = info[ind]
                    testBlock.blocks[i].timestamp = dat1 + " " + dat2
                    ind = ind + 1
                    testBolck.blocks[i].host = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].ip = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].pHash = info[ind]
                    ind = ind + 1
                    testBlock.blocks[i].cHash = info[ind]
                    ind = ind + 1
                 
                   
    #Sends chain update
    elif opt == "8":   
        space = " "
        HOST = input("specify IP ")  # The server's hostname or IP address
        PORT = 7023                 # The port used by the server
        pushLength = testBlock.getSize() + 1
        print (length)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            for i in range(0, pushLength):
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
                s.send(space.encode('utf-8'))
        
    #Exits GUI
    elif opt == "E" or opt == "e":
        run = False

    
    #Handles invalid input
    else:
        print("Invalid Option!")

    
    
