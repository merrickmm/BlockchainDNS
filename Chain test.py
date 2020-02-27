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
    print("\t[1] Create a new chain (Must be ran before option 2, 3, or 4)")
    print("\t[2] Add a block to a chain")
    print("\t[3] Print a chain")
    print("\t[4] Verify a chain")
    print("\t[5] Output to CSV")
    print("\t[6] Load chain from CSV")
    print("\t[7] Accept and print chain")
    print("\t[E]xit")
    opt = input("")

    #Create chain option(must be ran first)
    if opt == "1":
        testBlock = dnsChain()
        
    #Adds block to chain with given IP
    elif opt == "2":
        inIP = input("Enter the IP address: ")
        testBlock.addBlock(inIP)


    #Prints current block data of chain
    elif opt == "3":
        length = testBlock.getSize() + 1
        for i in range(0, length):
            print ("Index: ", testBlock.blocks[i].index)
            print (f"\tTimestamp: ", testBlock.blocks[i].timestamp)
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
        testBlock.chainWrite(length)

    #Loads Chain from a CSV file
    elif opt == "6":
        testBlock.chainRead()

    #Listens for chain update
    elif opt == "7":
        HOST = '127.0.0.1'  
        PORT = 7023        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            while True:
                data = acceptData(s)
                print (data)
                 
                   
                    
    #Exits GUI
    elif opt == "E" or opt == "e":
        run = False

    
    #Handles invalid input
    else:
        print("Invalid Option!")

    
    
