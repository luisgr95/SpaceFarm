def regarplantas():
    import RPi.GPIO as GPIO
    import serial
    import time
    import datetime
    import pyrebase
    config = {
     "apiKey": "AIzaSyAWkpaskMGuMgIYhn8ntly2sWbE0IseXhI",
    "authDomain": "spacefarm-a74ce.firebaseapp.com",
    "databaseURL": "https://spacefarm-a74ce.firebaseio.com",
    "storageBucket": "spacefarm-a74ce.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    arduino=serial.Serial ('/dev/ttyACM0', 115200)
    localtime = time.asctime( time.localtime(time.time()) )
    hora=time.strftime('%H:%M')
   
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(12.5)
       
    
    time.sleep(1)
    arduino.write("X10 Y10 Z10\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta1:  " + time.strftime('%H:%M')
    db.child("sembrar/planta1/Hregado").set(hora)
    arduino.write("X10 Y20\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta2:  " + time.strftime('%H:%M')
    db.child("sembrar/planta2/Hregado").set(hora)
    arduino.write("X25 Y10\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta3:  " + time.strftime('%H:%M')
    db.child("sembrar/planta3/Hregado").set(hora)
    arduino.write("X25 Y20\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta4:  " + time.strftime('%H:%M')
    db.child("sembrar/planta4/Hregado").set(hora)
    arduino.write("X40 Y10\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta5:  " + time.strftime('%H:%M')
    db.child("sembrar/planta5/Hregado").set(hora)
    arduino.write("X40 Y20\n")
    GPIO.output(17,True)
    time.sleep(5)
    GPIO.output(17,False)
    print "regado planta6:  " + time.strftime('%H:%M')
    db.child("sembrar/planta6/Hregado").set(hora)
    arduino.write("X0 Y0\n")
    print "Enviado regar"
    
