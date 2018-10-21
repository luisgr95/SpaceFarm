import serial
import time



arduino=serial.Serial ('/dev/ttyACM0', 115200)
time.sleep(1)

arduino.write("X0 Y0\n")
