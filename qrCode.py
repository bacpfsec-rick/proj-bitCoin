# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:05:26 2015

@author: Rick
    Using Python2.7
"""

import qrcode
import random as ran

class qrCode:
    def __init__(self):
        self.wallet = []  
        self.history = []
        self.numOfTypes = ran.randint(1,10)
        self.strWallet = ""
        self.randomWallet()
        self.randomHistory()
        
    def randomWallet(self):        
        for i in range(self.numOfTypes):
            t = (("Currency(" + str(i+1) + ")"),str(ran.randint(100,1000)))
            self.wallet.append(t)
    
    def randomHistory(self):
        date = 10
        for i in range(ran.randint(5,10)):
            r = ran.randint(0,1)
            if r == 1:
                sr = "From "
            else:
                sr = "Send "
            record = "Date(2015-07-" + str(date) + "): " + sr + \
                    "User(" + chr(64 + ran.randint(1,10)) + \
                    ") - Currency(" + str(ran.randint(1,self.numOfTypes)) + \
                    ") by " + str(ran.randint(10,100))
            date += ran.randint(1,2)
            self.history.append(record)
   
    def transIntoStr(self):
        self.strWallet += "Current Wallet:\n"
        for t in self.wallet:
            self.strWallet += (str(t[0]) + ':-:' + str(t[1]) + '\n')
        self.strWallet += "Transaction History:\n"
        for h in self.history:
            self.strWallet += (h + '\n')
    
    def showWallet(self):    
        self.transIntoStr()
        print(self.strWallet)
        
            
    def generateQR(self):
        img = qrcode.make(self.strWallet)
        img.save('walletQR.png')

def illustrateQrcode():
    qr = qrCode()
    qr.showWallet()
    print("The wallet in stored into QR code as walletQR.png")
    qr.generateQR()
    
if __name__ == "__main__":
    illustrateQrcode()