# -*- coding: utf-8 -*- 
#------------------------------------
# @calling
# @purpose : MQTT Pub, sample
# @date : 2016-04-01
# @Author : 
#------------------------------------
import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_mqttPub
import com_sendString
import zenhan

mTopic="item-kuc-arc-f/device-1/matrix_sample"

mTimeMax=5
mMaxTitle=10

mTyp_MSG =1
mTyp_TIME =2

if __name__ == "__main__":
	sMsgSample="サンプルもじ123"
	clsSend= com_sendString.sendStringClass()
	clsPub=com_mqttPub.mqttPubClass()
	from datetime import datetime
	tmBef = datetime.now()
	iTyp=mTyp_MSG
	
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		
		sTemp=""
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				if iTyp==mTyp_MSG:
					sTemp=clsSend.convert_zenkau(sMsgSample)
					print "sTemp1="+sTemp
					clsPub.send_pubw(sTemp ,mTopic)
				else:
					sHHMM = datetime.now().strftime("%H:%M")
					sTemp=clsSend.convert_zenkau("じかん　"+ sHHMM)
					print "sTemp2="+sTemp
					clsPub.send_pubw(sTemp ,mTopic)
				iTyp=iTyp+1
				if iTyp > 2:
					iTyp=mTyp_MSG
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


