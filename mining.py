# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:35:19 2015

@author: Rick
"""

# import myHash.py
import sys; 
if not "/" in sys.path:
    sys.path.append("/") 
if not 'myHash' in sys.modules:
    myHash = __import__('myHash')
else:
    eval('import myHash')
    myHash = eval('reload(myHash)')
import random as ran
import time

# def mining class    
class mining:
    def __init__(self):
        self.coin = 0        
        self.total = 0
        self.cKey = 1
        self.pool = myHash.myHash()        


    def draw(self):
        print("Current bitCoin pool: \n" + \
            "   ( B -> coin ) \n" + \
            "   (   -> undetected ) \n" + \
            "   ( X -> detected & failed ) \n" + \
            "   ( O -> detected & found ) ")
        for i in range(int(self.pool.cap/5)):
            print([kv[1] for kv in self.pool.data[i*5:(i+1)*5]])
        print("Current BitCoin mined: " + str(self.total) + "\n")

    def generateCoin(self):
        if self.coin == 0:
            print("Generate a new random coin in the mine field")
            self.pool.insert(ran.randint(self.cKey,self.pool.cap),'B')
            self.coin += 1
    
    def mine(self):
        for i in range(1,101):
            self.generateCoin()
            print("Mining the position with key-" + str(i) +":")
            result = self.pool.findK(i)
            if result == -1: # undetected
                print("The hashed position is empty!")
                self.pool.insert(i,'X')
            else: # found the B-coin
                print("The hashed position contains a BitCoin!")
                self.pool.data[result] = (i,'O')
                self.coin -= 1
                self.total +=1
            self.cKey += 1
            self.draw()
            time.sleep(2)

def illustrateMining():
    m = mining()
    m.mine()
    
if __name__ == "__main__":
    illustrateMining()    