def sembrarzanahoria():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
   
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(3.5)

    arduino.write("G00 X5 Y5 Z10\n") 
    time.sleep(5)
    arduino.write("G00 Z-5\n")
    time.sleep(5)
    
    GPIO.output(27, True)
    time.sleep(1)
    arduino.write("G00 Z10\n")

def sembrarpapa():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(3.5)

    arduino.write("G00 X10 Y5 Z10\n") 
    time.sleep(5)
    arduino.write("G00 Z-5\n")
    time.sleep(5)
    GPIO.output(27, True)
    time.sleep(1)
    arduino.write("G00 Z10\n")

def sembrarcebolla():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(3.5)
    
    arduino.write("G00 X15 Y5 Z10\n") 
    time.sleep(5)
    arduino.write("G00 Z-5\n")
    time.sleep(5)
    GPIO.output(27, True)
    time.sleep(1)
    arduino.write("G00 Z10\n")


def sembrarplanta1():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


    arduino.write("G00 X10 Y10 Z10\n")
    time.sleep(5)
    arduino.write("G00 Z-10\n")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G00 Z10\n")
    time.sleep(5)
    arduino.write("G00 X0 Y0 Z10\n")

def sembrarplanta2():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    
    planta2="G00 X20 Y20 Z10"
    origen="G00 X0 Y0 Z10"

    arduino.write(planta2)
    time.sleep(5)
    arduino.write("G00 Z-10")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G00 Z10")
    time.sleep(5)
    arduino.write(origen)

def sembrarplanta3():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    planta3="G00 X30 Y30 Z10"
    origen="G00 X0 Y0 Z10"

    arduino.write(planta3)
    time.sleep(5)
    arduino.write("G01 Z-10")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G01 Z10")
    time.sleep(5)
    arduino.write(origen)

def sembrarplanta4():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    planta4="G00 X40 Y40 Z10"
    origen="G00 X0 Y0 Z10"

    arduino.write(planta4)
    time.sleep(5)
    arduino.write("G00 Z-10")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G00 Z10")
    time.sleep(5)
    arduino.write(origen)

def sembrarplanta5():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    planta5="G00 X50 Y50 Z10"
    origen="G00 X0 Y0 Z10"

    arduino.write(planta5)
    time.sleep(5)
    arduino.write("G00 Z-10")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G00 Z10")
    time.sleep(5)
    arduino.write(origen)

def sembrarplanta6():
    import serial
    import RPi.GPIO as GPIO
    import time
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
     
    planta6="G00 X60 Y60 Z10"
    origen="G00 X0 Y0 Z10"

    arduino.write(planta6)
    time.sleep(5)
    arduino.write("G00 Z-10")
    time.sleep(5)
    GPIO.output(27,False)
    time.sleep(1)
    arduino.write("G00 Z10")
    time.sleep(5)
    arduino.write(origen)

