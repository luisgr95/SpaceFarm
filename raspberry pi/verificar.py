def verificarhumedadf():
    import pyrebase
    import serial
    import time
    import RPi.GPIO as GPIO
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    nano= serial.Serial ('/dev/ttyACM1', 9600)
    config = {
    "apiKey": "AIzaSyAWkpaskMGuMgIYhn8ntly2sWbE0IseXhI",
    "authDomain": "spacefarm-a74ce.firebaseapp.com",
    "databaseURL": "https://spacefarm-a74ce.firebaseio.com",
    "storageBucket": "spacefarm-a74ce.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(7.5)
    
    time.sleep(1)
    arduino.write("X10 Y5\n")
    time.sleep(2)
    arduino.write("Z-10\n")
    nano.write(humedadf)
    time.sleep(1)
    valor1 = nano.readline()
    print "Humedad planta 1=" + (valor1)
    db.child("sembrar/planta1/humedad").set(valor1.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("Z10\n")
    time.sleep(2)
    arduino.write("X10 Y15\n")
    time.sleep(2)
    arduino.write("Z-10\n")
    nano.write(humedadf)
    time.sleep(1)
    valor2= nano.readline()
    print "Humedad planta 2=" + (valor2)
    db.child("sembrar/planta2/humedad").set(valor2.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("G00\n Z10\n")
    time.sleep(2)
    arduino.write("X20 Y5\n")
    nano.write(humedadf)
    time.sleep(1)
    valor3=nano.readline()
    print "Humedad planta 3=" + (valor3)
    db.child("sembrar/planta3/humedad").set(valor3.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("G00\n Z-10\n")
    time.sleep(2)
    arduino.write("G00\n Z10\n")
    time.sleep(2)
    arduino.write("X20 Y15\n")
    nano.write(humedadf)
    time.sleep(1)
    valor4= nano.readline()
    print "Humedad planta 4=" + (valor4)
    db.child("sembrar/planta4/humedad").set(valor4.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("G00\n Z-10\n")
    time.sleep(2)
    arduino.write("G00\n Z10\n")
    time.sleep(2)
    arduino.write("X30 Y5\n")
    nano.write(humedadf)
    time.sleep(1)
    valor5=nano.readline()
    print "Humedad planta 5=" + (valor5)
    db.child("sembrar/planta5/humedad").set(valor5.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("G00\n Z-10\n")
    time.sleep(2)
    arduino.write("G00\n Z10\n")
    time.sleep(2)
    arduino.write("X30 Y15\n")
    nano.write(humedadf)
    time.sleep(1)
    valor6=nano.readline()
    print "Humedad planta 6=" + (valor6)
    db.child("sembrar/planta6/humedad").set(valor6.rstrip('\r\n') + "%")
    time.sleep(2)
    arduino.write("G00\n Z-10\n")
    time.sleep(2)
    arduino.write("G00\n Z10\n")
    time.sleep(2)
    arduino.write("X0 Y0\n")
