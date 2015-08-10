# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:47:57 2015

@author: Rick
    Using Python2.7
"""

import random as ran
import math as m

class blockchain:
    def __init__(self):
        self.greeting()
        self.userCount = 25
        # (0,4,4,10) is reserved for the main user0 in middle with 10 BitCoin
        self.userInfo = [(0,4,4,10)]
        self.records = [ [ ] for i in range(self.userCount+1)]
        self.network = [ ['  ' for i in range(0,9)] for j in range(0,9)]
        self.generateRandomUsers()
             
    def greeting(self):
        print("There are already 25 random BitCoin users in the network!")
        print("You are at the middle of the network with 10 BitCoins!")
    
    def generateRandomUsers(self):
        # put user0 into network
        self.network[4][4] = " 0"
        self.records[0].append("TRADE  --- Initial coin %d" % 10)
        # put userRandom into network
        for i in range(1,self.userCount+1):
            # generate user id
            if i<10:
                uid = " " + str(i)
            else:
                uid = str(i)
            pos = (4,4)
            while self.network[pos[0]][pos[1]] != '  ':
                pos = (ran.randint(0,8),ran.randint(0,8))
            self.network[pos[0]][pos[1]] = uid
            coin = ran.randint(1,10)
            self.userInfo.append((i,pos[0],pos[1],coin))
            self.records[i].append("TRADE  --- Initial coin %d" % coin)

    def showNetwork(self):
        print("User distribution in current network")
        for i in range(0,9):
            print(self.network[i])        
     
    def showUserInfo(self):
        print("Detailed user info")
        for i in range(len(self.userInfo)):
            tup = self.userInfo[i]
            print("User %d at (%d,%d) has coin %d" \
                %(tup[0],tup[1],tup[2],tup[3]))
            
    def checkUserRecord(self,no):
        print("Record of user-%d is listed as follow:" % no)
        for rec in self.records[no]:
            print(rec)
        print("Current coin balance : %d" % self.userInfo[no][3])
    
    def findNearby(self,no1,no2):
        uno1 = self.userInfo[no1]
        uno2 = self.userInfo[no2]
        affectRegion = []
        for user in self.userInfo:
            if uno1 == user or uno2 == user:
                continue
            if (m.pow((user[1]-uno1[1]),2)+m.pow((user[2]-uno1[2]),2)<=9):
                affectRegion.append(user[0])                
        return affectRegion

    def updateUser(self,no,amount):
        old = self.userInfo[no]
        new = (no,old[1],old[2],amount)
        self.userInfo[no] = new
    
    def trade(self,u,no):
        tradeType = raw_input("Trade type [S-Sell,B-Buy]: ")
        if tradeType == "S":
            limit = self.userInfo[u][3]
        elif tradeType == "B":
            limit = self.userInfo[no][3]
        else:
            print("Invalid option!")
            self.trade(no)       
        amount = int(raw_input("Valid trading amount [1~%d]: " % limit))
        source = self.userInfo[u]
        target = self.userInfo[no]     
        # Find the nearby users
        print("Transaction completed!")
        vUsers = self.findNearby(u,no)
        print("Verifications are sent to users:")
        print(vUsers)
        # Update the balance and record
        if tradeType == "S":
            self.updateUser(0,source[3]-amount)
            self.updateUser(no,target[3]+amount)
            self.records[0].append("TRADE  --- Sell %d to No.%d" \
                                    % (amount,no))
            self.records[no].append("TRADE  --- Buy %d from No.%d" \
                                    % (amount,u))
            for vu in vUsers:
                self.records[vu].append("VERIFY --- C %d from No.%d to No.%d" \
                                    % (amount,u,no))
        else: # Buy
            self.updateUser(0,source[3]+amount)
            self.updateUser(no,target[3]-amount)
            self.records[0].append("TRADE  --- Buy %d from No.%d" \
                                    % (amount,no))
            self.records[no].append("TRADE  --- Sell %d to No.%d" \
                                    % (amount,u))
            for vu in vUsers:
                self.records[vu].append("VERIFY --- %d from No.%d to No.%d)" \
                                    % (amount,no,u))                        
    
    def execute(self):
        while True:
            print("\nAvaliable options:")
            print("   N - Show the current network")
            print("   A - Check info of all users")
            print("   C - Check the record of a single user")
            print("   T - Trade with another user")
            print("   E - Exit the system")
            choice = raw_input("Select your choice (): ")
            if choice == "N":
                self.showNetwork()
            elif choice == "A":
                self.showUserInfo()
            elif choice == "C":
                no = int(raw_input("Select no. of target user [0~25]: "))
                self.checkUserRecord(no)
            elif choice == "T":
                no = int(raw_input("Select no. of target user [1~25]: "))
                self.trade(0,no)
            elif choice == "E":
                break
            else:
                print("Invalid option!")
        
            
def illustrateBlockchain():
    bc = blockchain()
    bc.execute()
    
    
if __name__ == "__main__":
    illustrateBlockchain()
        
        