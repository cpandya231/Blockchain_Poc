
# coding: utf-8

# In[2]:


import hashlib
import json
from datetime import datetime


class Block:
    def calculateHash(self):
        return hashlib.sha256((self.timestamp+str(self.transaction)+self.previoushash+str(self.nonce))
                              .encode('utf-8')).hexdigest()
        # return hashlib.sha256(("abc").encode('utf-8')).hexdigest()

    def __init__(self, timestamp, transaction, previoushash=''):
        print("Constructing a new block")
        
        self.timestamp = timestamp
        self.transaction = transaction
        self.previoushash = previoushash
        self.nonce = 0
        self.hash = self.calculateHash()
        
    #Proof of Work logic
    def mineBlock(self, newBlock, difficulty):
        #print(f"SubString {newBlock.hash[0:difficulty]}")

        while(str(newBlock.hash)[0:difficulty] != "0"*difficulty):
            newBlock.nonce += 1
            #print(f"New Hash {newBlock.calculateHash()}")
            newBlock.hash = newBlock.calculateHash()
        return newBlock

    def __str__(self):
        return "Timestamp: "+self.timestamp+" transaction: "+self.transaction+" Hash: "+self.hash


class BlockChain:

    def createGenesisBlock(self):
        initialTransactions=[Transaction("demo","XYZ", 0)]
        
        return Block("09-08-2018", initialTransactions)

    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 2 
        self.pendingTransaction=[]
        self.reward=100


    
    def minePendingTransactions(self,miningRewardAddress):
        
        newBlock=Block(str(datetime.now()),self.pendingTransaction)
        newBlock=newBlock.mineBlock(newBlock,self.difficulty)
        newBlock.previoushash=self.getLatestBlock().hash
        print("Block successfully mined!!")
        self.chain.append(newBlock)

        self.pendingTransaction=[
            Transaction("System",miningRewardAddress,self.reward)
        ]
   
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def createTransaction(self,transaction):
        self.pendingTransaction.append(transaction)

    def checkBalanceOfAddress(self,address):
        balance=0
        for block in self.chain:
            for tran in block.transaction:
                if(tran.fromAddress==address):
                    balance-=tran.amount
                elif(tran.toAddress==address):
                    balance+=tran.amount
        return balance

    def validateBlockChain(self):
        i = 1
        while(i < len(self.chain)):
            currblock = self.chain[i]
            prevBlock = self.chain[i-1]
            if(not currblock.hash == currblock.calculateHash()):
                return False
            
            if(not currblock.previoushash == prevBlock.hash):
                return False
            i += 1
        return True
    


class Transaction:
    def __init__(self,fromAddress,toAddress,amount):
        self.fromAddress=fromAddress
        self.toAddress=toAddress
        self.amount=amount
    def __str__(self):
        #return "From: "+self.fromAddress+" To: "+self.toAddress+" Amount: "+self.amount
        return self.__dict__

    


def obj_to_dict(obj):
    return obj.__dict__


blockChain = BlockChain()
blockChain.createTransaction(Transaction("ckp","abc",10))
blockChain.createTransaction(Transaction("abc","ckp",100))
print(json.dumps(blockChain.chain, default=obj_to_dict))
print("Starting miner!!")
blockChain.minePendingTransactions("ThePrime")
print(json.dumps(blockChain.chain, default=obj_to_dict))
print(f"Balance of abc {blockChain.checkBalanceOfAddress('abc')}")
print(f"Balance of ckp {blockChain.checkBalanceOfAddress('ckp')}")
print(f"Balance of ThePrime {blockChain.checkBalanceOfAddress('ThePrime')}")
print("Starting miner!!")
blockChain.minePendingTransactions("ThePrime")
print(f"Balance of ThePrime {blockChain.checkBalanceOfAddress('ThePrime')}")
