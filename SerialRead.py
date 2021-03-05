import os
import sys
import time
import serial

ser = serial.Serial(port='COM13', baudrate=115200, bytesize=serial.EIGHTBITS)

print()        
print("connected to: " + ser.portstr)
print()

while True:
    #line = ser.readline()
    print(ser.readline())
    #print()

ser.close()

