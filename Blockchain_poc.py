
# coding: utf-8

# In[2]:


import hashlib
import json
class Block:
    
    def calculateHash(self):
        return hashlib.sha256((str(self.index)+self.timestamp+self.data+self.previoushash).encode('utf-8')).hexdigest()
        #return hashlib.sha256(("abc").encode('utf-8')).hexdigest()
    
    def __init__(self,index, timestamp, data, previoushash=''):
        print("Constructing a new block")
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previoushash=previoushash
        self.hash=self.calculateHash()
        
    def __str__(self):
        return "Index: "+str(self.index)+" Timestamp: "+self.timestamp+" Data: "+self.data+" Hash: "+self.hash
    


class BlockChain:
    
    def createGenesisBlock(self):
        return Block(0,"09-08-2018","First Block","0")
    
    def __init__(self):
        self.chain=[self.createGenesisBlock()]
        
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self,newBlock):
        newBlock.previoushash=self.getLatestBlock().hash
        return self.chain.append(newBlock)
    def validateBlockChain(self):
        i=1
        while(i <len(self.chain)):
            currblock=self.chain[i]
            prevBlock=self.chain[i-1]
            #if(not currblock.hash == currblock.calculateHash()):
            #    print(f"Check1{currblock.hash}")
            #    print(f"Check2{currblock.calculateHash()}")
            #    return False
            if(not self.chain[i].previoushash==self.chain[i-1].hash):
                return False
            i+=1
        return True
        

def obj_to_dict(obj):
    return obj.__dict__

blockChain=BlockChain()
blockChain.addBlock(Block(1,"09-08-2018","Chintan's Data","0"))
blockChain.addBlock(Block(2,"09-08-2018","This tech is fucking awesome!!","0"))

type(blockChain.chain)
print(json.dumps(blockChain.chain,default=obj_to_dict))
print(f"Is the blockchain valid?{blockChain.validateBlockChain()}")












