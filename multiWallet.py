# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:28:37 2015

@author: Rick
    Using Python2.7
"""

import random as ran

class multiWallet:
    def __init__(self):
        self.wallet = []
        self.transaction = []
        self.randomGenerate()
    
    def randomGenerate(self):
        # generate coins
        self.wallet.append(('BitCoin',ran.randint(50,100)))
        self.wallet.append(('LitCoin',ran.randint(50,100)))
        self.wallet.append(('EccCoin',ran.randint(50,100)))
        self.wallet.append(('  USD  ',ran.randint(100,500)))
        self.wallet.append(('  RMB  ',ran.randint(1000,5000)))
           
    def showDetail(self):
        print("---Current Wallet---")
        for w in self.wallet:
            print(w[0] + " :-: " + str(w[1]))
        print("---Transaction History---")
        for t in self.transaction:
            print(t)
        print("")   
    
    def trade(self,targets,tid,ratios):         
        print("\n   B-Buy currency    S-Sell currency    Q-Quit trading")
        tradeType = raw_input("Select your trade type: ")
        if tradeType == "Q":
            return
        print("\n   B-BitCoin   L-LitCoin   E-EccCoin   U-USD   R-RMB")        
        cMap = {"B":0,"L":1,"E":2,"U":3,"R":4}
        mType = raw_input(">>:Select the currency from your wallet: ")
        mIndex = cMap[mType]
        tType = raw_input(">>:Select the currency from his wallet: ")
        tIndex = cMap[tType]
        if tradeType == "B":
            ratio = ratios[mIndex][tIndex]
            maxAmount = min(round(1.0*self.wallet[mIndex][1]*ratio,4), \
                            round(1.0*targets[tid].wallet[tIndex][1],4))
            amount = float(raw_input(">>:Select the amount to buy (0~" \
                            + str(maxAmount) + "): "))                            
            oriAmount = round(amount/ratio,4)
            self.wallet[mIndex] = (self.wallet[mIndex][0],\
                                    self.wallet[mIndex][1]-oriAmount)
            self.wallet[tIndex] = (self.wallet[tIndex][0],\
                                    self.wallet[tIndex][1]+amount)
            targets[tid].wallet[mIndex] = (targets[tid].wallet[mIndex][0],\
                                    targets[tid].wallet[mIndex][1]+oriAmount)
            targets[tid].wallet[tIndex] = (targets[tid].wallet[tIndex][0],\
                                    targets[tid].wallet[tIndex][1]-amount)                                  
            # generate transaction record
            self.transaction.append("Buy " + tType + "(" + str(amount) + ")" \
                                + "from User(" + str(tid+1) + ") with " \
                                + mType + "(" + str(oriAmount) + ")")
            targets[tid].transaction.append("Sell " + mType + "(" \
                                + str(oriAmount) + ") to User(0) with " \
                                + tType + "(" + str(amount) + ")")
        else: # case for selling
            ratio = ratios[mIndex][tIndex]
            maxAmount = min(round(1.0*self.wallet[mIndex][1],4), \
                            round(1.0*targets[tid].wallet[tIndex][1]/ratio,4))
            amount = float(raw_input(">>:Select the amount to sell (0~" \
                            + str(maxAmount) + "): "))                            
            excAmount = round(amount*ratio,4)
            self.wallet[mIndex] = (self.wallet[mIndex][0],\
                                    self.wallet[mIndex][1]-amount)
            self.wallet[tIndex] = (self.wallet[tIndex][0],\
                                    self.wallet[tIndex][1]+excAmount)
            targets[tid].wallet[mIndex] = (targets[tid].wallet[mIndex][0],\
                                    targets[tid].wallet[mIndex][1]+amount)
            targets[tid].wallet[tIndex] = (targets[tid].wallet[tIndex][0],\
                                    targets[tid].wallet[tIndex][1]-excAmount)                                  
            # generate transaction record
            self.transaction.append("Sell " + tType + "(" + str(amount) + ")" \
                                + "to User(" + str(tid+1) + ") with " \
                                + mType + "(" + str(excAmount) + ")")
            targets[tid].transaction.append("Buy " + mType + "(" \
                                + str(excAmount) + ") from User(0) with " \
                                + tType + "(" + str(amount) + ")")
        print("\n   Transaction is completed\n")                                

# generate random trading ration between 5 currencies
def randomRatio():
    ratio = [ [1] * 5 for i in range(5)] 
    for i in range(5):
        for j in range(i+1,3):
            r = ran.randint(1,3)
            ratio[i][j] = r
            ratio[j][i] = round(1.0/r,4)
        if i != 3:
            r3 = ran.randint(5,10)
            ratio[i][3] = r3
            ratio[3][i] = round(1.0/r3,4)
        if i != 4:
            r4 = ran.randint(25,50)
            ratio[i][4] = r4
            ratio[4][i] = round(1.0/r4,4)
    return ratio

def illustrateMultiWallet():
    # generate current trading ratio
    rr = randomRatio()
    print("   Current trading ratio")    
    print(" \tB\tL\tE\tU\tR")
    colName = ["B","L","E","U","R"]
    for i in range(5):
        print("%s\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f" %(colName[i],rr[i][0],\
                            rr[i][1],rr[i][2],rr[i][3],rr[i][4]))
    print("\n")
    # generate my wallet
    me = multiWallet()
    print("   Info of the wallet owner")
    me.showDetail()    
    print("\n")
    # generate 5 trading targets
    targets = [multiWallet() for i in range(5)]    
    while True:
        print("***Welcome to the trading system***")        
        targetId = int(raw_input(">>:Select user ID from 1~5, or 0 to quit: "))
        if targetId == 0:
            break
        me.trade(targets,targetId-1,rr)     
    # print the wallets after trading
    print("***All tradings are completed, current users' wallets***")
    print("   Info of the wallet owner")
    me.showDetail()
    for no in range(5):
        print("   Info of the user(" + str(no+1) + ")")
        targets[no].showDetail()
    
if __name__ == "__main__":
    illustrateMultiWallet()    
    