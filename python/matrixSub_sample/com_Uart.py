# -*- coding: utf-8 -*- 
import serial
#import com_appConst
import time


#mMaxOne =10
#mCount=0

#com_Uart
class uartClass:
    #define
    mCount=0
    def __init__(self):
        print ""
    
    def send_matrix(self, sOne, ser):
    	ser.write(sOne)
    	self.mCount=self.mCount+1
    	if (self.mCount>=2):
    		time.sleep(0.1)
    		self.mCount=0

    def send_sub(self, sPay ,ser):
    	self.mCount=0
    	self.send_matrix("011", ser)
    	for idx in range(len(sPay)):
    		char_code = ord(sPay[idx])
    		#sCode= str(char_code)
    		sHcode= str( hex(char_code) )
    		sBuf = sHcode.replace('0x', '')
    		print sBuf
    		self.send_matrix(sBuf, ser)
    	self.send_matrix("\r\n", ser)
