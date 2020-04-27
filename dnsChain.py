import hashlib
import datetime
import csv

#Creates block object to be added to chain
class dnsBlock():

    #Initializes block object
    def __init__(self, index, host, ip, pHash):
        self.index = index
        self.timestamp = datetime.datetime.utcnow()
        self.ip = ip
        self.host = host
        self.pHash = pHash
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.ip).encode('utf-8'))
        key.update(str(self.pHash).encode('utf-8'))
        cHash = key.hexdigest()
        self.cHash = cHash


#Creates Chain object
class dnsChain():

    #Initializes chain object
    def __init__(self): 
        self.blocks = [self.genesisBlock()]

    #Creates genesis block at index 0
    def genesisBlock(self): 
        return dnsBlock(0, 'Genesis', 'arbitrary', 'arbitrary')

    #Adds block to chain, takes IP
    def addBlock(self, host, ip):
        self.blocks.append(dnsBlock(len(self.blocks), host, ip, self.blocks[len(self.blocks)-1].cHash))

    #Returns size of chain in Blocks (excluding genesis)
    def getSize(self):
        return len(self.blocks)-1

    #Verifies that data is consistent between blocks
    def verify(self): 
        flag = True
        for i in range(1,len(self.blocks)):

            if self.blocks[i].index != i:
                flag = False
                print(f'Wrong block index at block {i}.')
            else:
                print(f'Right block index at block {i}.')
                
            if self.blocks[i-1].cHash != self.blocks[i].pHash:
                flag = False
                print(f'Wrong previous hash at block {i} or current at {i-1}.')
            else:
                print(f'Right hashes at {i} and {i-1}.')

            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                print(f'Backdating at block {i}.')
            else:
                print(f'No backdating at block {i}.')
            print("")
                
        return flag

    #Writes chain to a CSV file
    def chainWrite(self, cLen):
        with open('chain.csv', 'w', newline='') as csvfile:
            chainwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            chainwriter.writerow(['index', 'timestamp', 'host', 'ip', 'pHash', 'cHash'])
            for i in range(cLen):
                chainwriter.writerow([self.blocks[i].index, self.blocks[i].timestamp, self.blocks[i].host, self.blocks[i].ip, self.blocks[i].pHash, self.blocks[i].cHash])
                print("success index ", i)

    #Loads chain from CSV file
    def chainRead(self):
        with open('chain.csv', 'r', newline='') as csvfile:
            chainreader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for idx, row in enumerate(chainreader):
                if idx == 0:
                    continue
                elif idx == 1:
                    blockList = row
                    print(blockList)
                    self.blocks[idx-1].index = blockList[0]
                    self.blocks[idx-1].timestamp = blockList[1]
                    self.blocks[idx-1].host = blockList[2]
                    self.blocks[idx-1].ip = blockList[3]
                    self.blocks[idx-1].pHash = blockList[4]
                    self.blocks[idx-1].cHash = blockList[5]
                else:
                    self.blocks.append(dnsBlock("test", "test", "test", "test"))
                    blockList = row
                    print(blockList)
                    self.blocks[idx-1].index = blockList[0]
                    self.blocks[idx-1].timestamp = blockList[1]
                    self.blocks[idx-1].host = blockList[2]
                    self.blocks[idx-1].ip = blockList[3]
                    self.blocks[idx-1].pHash = blockList[4]
                    self.blocks[idx-1].cHash = blockList[5]



                    
