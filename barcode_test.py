from naoqi import *
import time

# Get a proxy on ALBarcodeReader

ROBOT_IP="192.168.1.105"
barcode=ALProxy("ALBarcodeReader", ROBOT_IP, 9559)
memory=ALProxy("ALMemory", ROBOT_IP, 9559)
broker = ALBroker("pythonBroker", "0.0.0.0", 0, ROBOT_IP, 9559)

# Handler class
class myEventHandler(ALModule):
  def myCallback(self, key, value, msg):
    print "Received \"" + str(key) + "\" event with data: " + str(value)

    # print(string)
    # print(string[:string.index(",")])



# Subscribe to the event (this will start the module)
handlerModule = myEventHandler("handlerModule")
memory.subscribeToEvent("BarcodeReader/BarcodeDetected", "handlerModule", "myCallback")

time.sleep(5) # Keep the broker alive for 20 seconds

# Unsubscribe to event
memory.unsubscribeToEvent("BarcodeReader/BarcodeDetected", "handlerModule")



qrcode = myEventHandler()
qrcode.myCallback()