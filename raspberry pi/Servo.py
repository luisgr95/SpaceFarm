def posverificar():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(7.5)

def posregar():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(12.5)

def possembrar():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)   
    p = GPIO.PWM(22,50)        
    p.start(2.5)

