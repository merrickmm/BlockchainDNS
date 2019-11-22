from dnsChain import *

#sets while conditional to true
run = True

#start GUI loop and prints options
while run == True:
    print("Select one of the following options: ")
    print("\t[1] Create a new chain (Must be ran before option 2, 3, or 4)")
    print("\t[2] Add a block to a chain")
    print("\t[3] Print a chain")
    print("\t[4] Verify a chain")
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

    #Exits GUI
    elif opt == "E" or opt == "e":
        run = False

    #Handles invalid input
    else:
        print("Invalid Option!")