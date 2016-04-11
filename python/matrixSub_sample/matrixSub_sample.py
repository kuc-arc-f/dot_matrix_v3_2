# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt
import serial
import com_Uart
import sys
import traceback

#import com_sensor
mTopic="item-kuc-arc-f/device-1/matrix_sample"

mDevice = "/dev/ttyAMA0"
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(topic=mTopic )
	#client.subscribe(topic="item/#")

#
def on_message(client, userdata, msg):
	ser=serial.Serial(mDevice ,9600)
	clsUart = com_Uart.uartClass()
	try:
			print("on_message:topic=" + msg.topic+" ,pay="+str(msg.payload))
			clsUart.send_sub(str(msg.payload) ,ser)
	except:
		print "--------------------------------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "--------------------------------------------"

if __name__ == "__main__":
#client = mqtt.Client()
    client = mqtt.Client(client_id="spam")
    
    client.on_connect = on_connect
    client.on_message = on_message
#    client.connect(host="localhost", port=1883)
    client.connect(host="test.mosquitto.org", port=1883)
    client.loop_forever()
#client.connect(host="localhost", port=1883)

 

