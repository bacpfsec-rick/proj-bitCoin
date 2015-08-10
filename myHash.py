# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:30:44 2015

@author: Rick
    Using Python2.7
"""

import time

# Definition of class myHash
class myHash:
    def __init__(self):
        # init
        self.size = 0
        self.cap = 5 
        self.alpha = 0.7   
        self.data = [(0," ")] *self.cap
     
    
    def hashFunc(self,k):
        return (k*k*k) % self.cap
    
    def insert(self,k,v):
        # inser then check the size
        pos = self.hashFunc(k)
        while self.data[pos][0] != 0:
            pos = (pos+1)%self.cap
        self.data[pos] = (k,v)
        self.size += 1
        if (self.size/self.cap>=self.alpha):
            self.rehash()        
            
    def rehash(self):
        print("Rehash old map of size " + str(self.cap) + \
        " into new map of size " + str(self.cap*2))
        self.cap *= 2 
        newData = [(0," ") for i in range(self.cap)]        
        for kv in self.data:
            if kv[0] != 0:
                pos = self.hashFunc(kv[0])
                while newData[pos][0] != 0:
                    pos = (pos+1)%self.cap
                newData[pos] = kv
        self.data = newData                
        self.size += 1

    def findK(self,k):
        count = 0
        pos = self.hashFunc(k)
        while self.data[pos][0] != k:
            pos = (pos+1)%self.cap
            count += 1
            if count == self.cap:
#                print("Key (" + str(k) + ") is not found!")
                return -1
        return pos

    def getV(self,k):
        pos = self.findK(k)
        if pos == -1:
            return ""
        else:
            return self.data[pos][1]        

    def updateKV(self,k,v):
        pos = self.findK(k)        
        self.data[pos] = (k,v)
    
    
        
# function for illustration of hash mechanism       
def illustrateHash():
    mh = myHash()        
    for i in range(1,101):
        print("Hashing value " + str(i) + " into HashTable:")
        print("Original hashed position: " + str(mh.hashFunc(i)+1))
        mh.insert(i,i)
        array = [kv[1] for kv in mh.data]
        print("Current hashtable:")        
        print(array)
        print("\n")
        time.sleep(2)
        
if __name__ == "__main__":
    illustrateHash()