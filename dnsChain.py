import hashlib
import datetime

class dnsBlock():
    def __init__(self, index, ip, pHash):
        self.index = index
        self.timestamp = datetime.datetime.utcnow()
        self.ip = ip
        self.pHash = pHash
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.ip).encode('utf-8'))
        key.update(str(self.pHash).encode('utf-8'))
        cHash = key.hexdigest()
        self.cHash = cHash

def blockTest(index, ip, pHash):
    block1 = dnsBlock(index, ip, pHash)

    print(block1.index)
    print(block1.timestamp)
    print(block1.ip)
    print(block1.pHash)
    print(block1.cHash)

class dnsChain():

    def __init__(self): 
        self.blocks = [self.genesisBlock()]
    
    def genesisBlock(self): 
        return dnsBlock(0, 'Genesis', 'arbitrary')


    def addBlock(self, ip):
        self.blocks.append(dnsBlock(len(self.blocks), ip, self.blocks[len(self.blocks)-1].cHash))

    def getSize(self):
        return len(self.blocks)-1

    def verify(self): 
        flag = True
        for i in range(1,len(self.blocks)):

            if self.blocks[i].index != i:
                flag = False
                print(f'Wrong block index at block {i}.')
            else:
                print(f'Right block index at block {i}.')
                
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                print(f'Wrong previous hash at block {i} or current at {i-1}.')
            else:
                print(f'Right hashes at {i} and {i-1}.')

            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                print(f'Backdating at block {i}.')
            else:
                print(f'No backdating at block {i}.')
                
        return flag 



                    
