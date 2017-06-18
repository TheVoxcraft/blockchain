import pickle
import hashlib
import time
import random
import string

class Block:
    def __init__(self, _data, _prev, _genesis=False):
        time_precision=100000
        self.data=_data
        self.timestamp=int(time.time()*time_precision)
        self.uniqueID=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
        self.prev_block=_prev
        self.genesis = _genesis
        if self.genesis:
            self.prev_block=self.uniqueID

class Blockchain:
    self.loaded=False
    self.blockchain=[]
    self.blockchain_file_name=""

    def __init__(self, _fo="blockchain.p"):
        self.blockchain_file_name=_fo
    
    def loadFromFile(self):
        try:
            print("(info) loading blockchain...")
            self.blockchain = pickle.load(open(self.blockchain_file_name, "rb"))
            self.loaded=True
        except (OSError, IOError) as e:
            print("(error) could not load blockchain...")
            self.loaded=False

    def saveToFile(self, fo=self.blockchain_file_name):
        print("(info) saving new blockchain...")
        pickle.dump(self.blockchain, open(self.blockchain_file_name, "wb"))
        
    def new(self):
        print("(info) creating new blockchain...")
        self.blockchain = []
        self.blockchain.append(Block("", "") ) # Genesis block

    def appendBlock(self, data, prev="_auto"):
        if prev=="_auto":
            prev=blockchain[len(blockchain)-1].uniqueID
        else:
            valid=False
            for i in self.blockchain:
                if i.uniqueID == prev and getChainSize(i.uniqueID) < 1:
                    valid=True
                    break
            if valid:
                self.blockchain.append(Block(data, prev))
            else:
                print("(error) could not append to chain ["+prev+"]")
        

    def appendChain(self, chain):
        chain_prev = chain[0].uniqueID
        valid=False
        for i in self.blockchain:
            if i.uniqueID == chain_prev and getChainSize(i.uniqueID) < 1:
                valid=True
                break
        if valid:
            self.blockchain.extend(chain)

        
    def getChainSize(self, ID):
        size = 0
        current = ID
        i=0
        while i < self.blockchain:
            if self.blockchain[i].prev == ID:
                size=size+1
                current=i.uniqueID
                i=0
            i=i+1
        return size
