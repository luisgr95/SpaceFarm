import pyrebase
import serial
import RPi.GPIO as GPIO
import time
import regar
import verificar
import sembrar
import datetime
import humedadr

config = {
"apiKey": "AIzaSyBKyF4N527SKUnHf4WCHPNS_6sMkdZuI-o",
"authDomain": "ecofarm-ee936.firebaseapp.com",
"databaseURL": "https://ecofarm-ee936.firebaseio.com",
"storageBucket": "ecofarm-ee936.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
fecha= datetime.date.today()
hoy= fecha.strftime("%d/%m/%Y")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)




while True:


    
    time.sleep(1)



    humedadr.verificarhumedadr()
			
    Estadoregar= db.child("regar").get()
    while (Estadoregar.val() == "true"):
     	regar.regarplantas()
     	db.child("regar").set("false")   
        
        break

    Estadoverificar= db.child("verificar").get()
    while (Estadoverificar.val() == "true"):
    	verificar.verificarhumedadf()
    	db.child("verificar").set("false")
        break
    

    Estadosembrar= db.child("sembrar/sembrar").get()
    while (Estadosembrar.val() == "true"):

        Sembrarp1=db.child("sembrar/planta1/sembrado").get()
        if (Sembrarp1.val() == "zanahoria"):
            sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta1()
    	    db.child("sembrar/planta1/sembrado").set("Zanahoria")
    	    print "Planta 1 : Zanahoria"
    	    db.child("sembrar/planta1/Fsembrado").set(hoy)


    	elif (Sembrarp1.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta1()
    	    db.child("sembrar/planta1/sembrado").set("Papa")
    	    print "Planta 1 : Papa"
    	    db.child("sembrar/planta1/Fsembrado").set(hoy)

    	elif (Sembrarp1.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta1()
    	    db.child("sembrar/planta1/sembrado").set("Cebolla")
    	    print "Planta 1 : Cebolla"
    	    db.child("sembrar/planta1/Fsembrado").set(hoy)

        break


    while (Estadosembrar.val() == "true"):

        Sembrarp2=db.child("sembrar/planta2/sembrado").get()
        if (Sembrarp2.val() == "zanahoria"):
    	    sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta2()
    	    db.child("sembrar/planta2/sembrado").set("Zanahoria")
    	    print "Planta 2 : Zanahoria"
    	    db.child("sembrar/planta2/Fsembrado").set(hoy)

        elif (Sembrarp2.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta2()
    	    db.child("sembrar/planta2/sembrado").set("Papa")
    	    print "Planta 2 : Papa"
    	    db.child("sembrar/planta2/Fsembrado").set(hoy)

        elif (Sembrarp2.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta2()
    	    db.child("sembrar/planta2/sembrado").set("Cebolla")
    	    print "Planta 2 : Cebolla"
    	    db.child("sembrar/planta2/Fsembrado").set(hoy)

        break


    while (Estadosembrar.val() == "true"):

        Sembrarp3=db.child("sembrar/planta3/sembrado").get()
        if (Sembrarp3.val() == "zanahoria"):
            sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta3()
    	    db.child("sembrar/planta3/sembrado").set("Zanahoria")
    	    print "Planta 3 : Zanahoria"
    	    db.child("sembrar/planta3/Fsembrado").set(hoy)

        elif (Sembrarp3.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta3()
    	    db.child("sembrar/planta3/sembrado").set("Papa")
    	    print "Planta 3 : Papa"
    	    db.child("sembrar/planta3/Fsembrado").set(hoy)

        elif (Sembrarp3.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta3()
    	    db.child("sembrar/planta3/sembrado").set("Cebolla")
    	    print "Planta 3 : Cebolla"
    	    db.child("sembrar/planta3/Fsembrado").set(hoy)

        break    	



    while (Estadosembrar.val() == "true"):

        Sembrarp4=db.child("sembrar/planta4/sembrado").get()
        if (Sembrarp4.val() == "zanahoria"):
            sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta4()
    	    db.child("sembrar/planta4/sembrado").set("Zanahoria")
    	    print "Planta 4 : Zanahoria"
    	    db.child("sembrar/planta4/Fsembrado").set(hoy)

        elif (Sembrarp4.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta4()
    	    db.child("sembrar/planta4/sembrado").set("Papa")
    	    print "Planta 4 : Papa"
    	    db.child("sembrar/planta4/Fsembrado").set(hoy)

        elif (Sembrarp4.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta4()
    	    db.child("sembrar/planta4/sembrado").set("Cebolla")
    	    print "Planta 4 : Cebolla"
    	    db.child("sembrar/planta4/Fsembrado").set(hoy)

        break
    	    


    while (Estadosembrar.val() == "true"):

        Sembrarp5=db.child("sembrar/planta5/sembrado").get()
        if (Sembrarp5.val() == "zanahoria"):
    	    sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta5()
    	    db.child("sembrar/planta5/sembrado").set("Zanahoria")
    	    print "Planta 5 : Zanahoria"
    	    db.child("sembrar/planta5/Fsembrado").set(hoy)

        elif (Sembrarp5.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta5()
    	    db.child("sembrar/planta5/sembrado").set("Papa")
    	    print "Planta 5 : Papa"
    	    db.child("sembrar/planta5/Fsembrado").set(hoy)

        elif (Sembrarp5.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta5()
    	    db.child("sembrar/planta5/sembrado").set("Cebolla")
    	    print "Planta 5 : Cebolla"
    	    db.child("sembrar/planta5/Fsembrado").set(hoy)

        break


    while (Estadosembrar.val() == "true"):

        Sembrarp6=db.child("sembrar/planta6/sembrado").get()
        if (Sembrarp6.val() == "zanahoria"):
    	    sembrar.sembrarzanahoria()
    	    sembrar.sembrarplanta6()
    	    db.child("sembrar/planta6/sembrado").set("Zanahoria")
    	    print "Planta 6 : Zanahoria"
    	    db.child("sembrar/planta6/Fsembrado").set(hoy)

        elif (Sembrarp6.val() == "papa"):
    	    sembrar.sembrarpapa()
    	    sembrar.sembrarplanta6()
    	    db.child("sembrar/planta6/sembrado").set("Papa")
    	    print "Planta 6 : Papa"
    	    db.child("sembrar/planta6/Fsembrado").set(hoy)

        elif (Sembrarp6.val() == "cebolla"):
    	    sembrar.sembrarcebolla()
    	    sembrar.sembrarplanta6()
    	    db.child("sembrar/planta6/sembrado").set("Cebolla")
    	    print "Planta 6 : Cebolla"
    	    db.child("sembrar/planta6/Fsembrado").set(hoy)

        break



    	

    




        
	



