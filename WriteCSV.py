import csv
from dnsChain import *
def chainWrite(cLen):
    
    with open('chain.csv', 'w') as csvfile:
        chainwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        chainwriter.writerow(['index', 'timestamp', 'ip', 'pHash', 'cHash'])
        for i in range(cLen):
            print("success index ", i)    
        
chainWrite(6)
