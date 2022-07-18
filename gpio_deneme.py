import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

GPIO.output(5, GPIO.LOW)

#GPI0.
#GPIO.output(3, GPIO.HIGH)

while(1):
    
    if(GPIO.input(5)):
        #print("high")
        try:
            import start
        except:
            print("error")
            continue
            
    else:
        print("low")
        
    
    
    #GPIO.OUT(3, GPIO.LOW)
    
    #GPIO.output(3, GPIO.LOW)

    #if(GPIO.input(3)==GPIO.LOW):
     #   print("b")
