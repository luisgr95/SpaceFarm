def verificarhumedadr():
    import pyrebase
    import serial
    import time
    import RPi.GPIO as GPIO
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
    nano.write("humedadr")
    time.sleep(1)
    valor = nano.readline()
    db.child("temperaturar").set(valor.rstrip('\r\n')+"%")
    

