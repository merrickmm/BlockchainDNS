import hashlib

class dnsBlock():
    def __init__(self, index, timestamp, ip, pHash, cHash):
        self.index = index
        self.timestamp = timestamp
        self.ip = ip
        self.pHash = pHash
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.ip).encode('utf-8'))
        key.update(str(self.pHash).encode('utf-8'))
        cHash = key.hexdigest()
        self.cHash = cHash

def blockTest(index, timestamp, ip, pHash):
    block1 = dnsBlock(index, timestamp, ip, pHash, None)

    print("Index: ", block1.index)
    print("Timestamp: ", block1.timestamp)
    print("IP: ", block1.ip)
    print("Previous Hash: ", block1.pHash)
    print("Current Hash: ", block1.cHash)

x = True
while x == True:
    index = input("Enter Index: ")
    timestamp = input("Enter Timestamp: ")
    ip = input("Enter IP: ")
    pHash = input("Enter pHash: ")
    blockTest (index, timestamp, ip, pHash)
