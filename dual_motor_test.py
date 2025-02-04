#https://github.com/Axel-Germany/Micropython_Pico_DRV8825/edit/main/Pico-DRV8825.py
from time import sleep
from machine import Pin
#STEPPER CONECTION
#RESET both conected with 3.3V                             VMOT       12V+  
led = Pin(25, Pin.OUT)         
#SLEEP both conected with 3.3V                             GROUND MOT 12V-
pSTEP_R = Pin(5, Pin.OUT)    # create output pin on GPIO16  B2 coilB red    NEMA14
pDIR_R = Pin(6, Pin.OUT)     # create output pin on GPIO17  B1 coilB blue   NEMA14
pEN_R = Pin(7, Pin.OUT)      # create output pin on GPIO18  A1 coilA black  NEMA14


pSTEP_L = Pin(2, Pin.OUT)    # create output pin on GPIO16  B2 coilB red    NEMA14
pDIR_L = Pin(1, Pin.OUT)     # create output pin on GPIO17  B1 coilB blue   NEMA14
pEN_L = Pin(0, Pin.OUT)  
#                                                          A2 coilA green  NEMA14           
#                                                          GROUND LOGIC  conected to PICO-Ground

steps = 250 # number of steps
usDelay = 1000 # number of microseconds
uS = 0.000001 # one microsecond


pEN_R.off()  #EN off switches motor on
pEN_L.off()  #EN off switches motor on


def turnstepperLcw(Msteps):
    pEN_L.off()  #EN allows power to stepper
    pDIR_L.off()        
    for i in range(Msteps):
        pSTEP_L.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP_L.off()                # set pin to lowlevel
        sleep(uS * usDelay)
    sleep(0.5)
    print("Left Motor turned CW")
    pEN_L.on()  #EN on takes power away from stepper   
def turnstepperLccw(Msteps):        
    pDIR_L.on()
    pEN_L.off()  #EN allows power to stepper
    for i in range(Msteps):
        pSTEP_L.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP_L.off()                # set pin to low level
        sleep(uS * usDelay)
    sleep(0.5)
    print("Motor turned CCW")
    pEN_L.on()  #EN on takes power away from stepper

def turnstepperRcw(Msteps):
    pEN_R.off()  #EN allows power to stepper
    pDIR_R.off()        
    for i in range(Msteps):
        pSTEP_R.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP_R.off()                # set pin to lowlevel
        sleep(uS * usDelay)
    sleep(0.5)
    print("Right Motor turned CW")
    pEN_R.on()  #EN on takes power away from stepper   
def turnstepperRccw(Msteps):        
    pDIR_R.on()
    pEN_R.off()  #EN allows power to stepper
    for i in range(Msteps):
        pSTEP_R.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP_R.off()                # set pin to low level
        sleep(uS * usDelay)
    sleep(0.5)
    print("Right Motor turned CCW")
    pEN_R.on()  #EN on takes power away from stepper





try: # Main program loop
    while True:
        print("stop loop with Ctrl + C")
        turnstepperRcw(steps)
        turnstepperLcw(steps)
        led.toggle()
        sleep(1.5)
        turnstepperLccw(steps)
        turnstepperRccw(steps)
    
# Scavenging work after the end of the program
except KeyboardInterrupt:
    pEN_L.on()
    pEN_R.on()    #EN on switches power on motor of
    print("fertig")
    
