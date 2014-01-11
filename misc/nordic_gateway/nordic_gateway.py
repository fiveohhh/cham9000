#!/usr/bin/python
import RPi.GPIO as GPIO
import spidev
import time
import urllib2


GPIO.setmode(GPIO.BOARD)
# Using board pin 13 for nordic interrupt line
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.OUT)

# Set CE HIGH
GPIO.output(15, GPIO.HIGH)


# Initialize device 0 on bus zero
radio = spidev.SpiDev(0,0)

def initRadio():
    # set data rate
    radio.xfer2([0x26, 0x06])
    # reset/clear
    radio.xfer2([0x20, 0x70])
    # Flush buffers
    radio.xfer2([0xE1])
    radio.xfer2([0xE2])
    # Enable Shockburst on all channels
    radio.xfer2([0x21, 0x7f])
    # Set pipe 1 rx address
    radio.xfer2([0x22, 0x03])
    radio.xfer2([0x2B,0xE7, 0xE7, 0xE7, 0xE7, 0xE7])
    # Enable pipe 1
    radio.xfer2([0x22, 0x02])
    # Enable dynamic payloads
    radio.xfer2([0x3D, 0x04])
    # On pipe 1
    radio.xfer2([0x3C, 0x02])
    # Power up and set to RX
    radio.xfer2([0x20, 0x0B])
    # Wait for crystal (really only needs to be ~ 4ms
    time.sleep(1)
    # Reset/clear
    radio.xfer2([0x27, 0x70])
    # Flush buffers
    radio.xfer2([0xE1])
    radio.xfer2([0xE2])


def handleMsgReceived(channel):
    print("message received")
    status = radio.xfer2([0xFF])[0]
    print("pipe: " + str(((status > 1)&0x07)))
    length = radio.xfer2([0x60,0xff])[1]
    print("Length: " + str(length))
    txData = [0x61]
    for i in range(length + 1):
        txData.append(0xff)
    raw = radio.xfer2(txData)[1:length+1]
    msg = ''.join(chr(i) for i in raw)
    print("Contents: " + str(msg))
    if msg.startswith("TMP"):
        #0 == 48
        #1 == 49
        newMsg = "TMP"
        if msg[3:5] == "00":
            newMsg += "48"
        elif msg[3:5] == "01":
            newMsg += "49"
        newMsg += msg[5:10]
        print newMsg
        try:
            response =  urllib2.urlopen("http://10.12.34.135/restInterface/msg/" + newMsg + '/' )
            print(response)
        except urllib2.HTTPError, e:
            print "exception occurred"
    radio.xfer2([0x27,0x70])
    radio.xfer2([0xe1])
    radio.xfer2([0xe2])




def main():
    initRadio()
    GPIO.add_event_detect(13,GPIO.FALLING)
    GPIO.add_event_callback(13,handleMsgReceived)
    while(True):
        time.sleep(10)
	pass









if __name__ == "__main__":
    main()


