from stepper import Stepper
import time
from machine import Pin

s1 = Stepper(2,1,0, steps_per_rev=200,speed_sps=5)
s2 = Stepper(5,6,7, steps_per_rev=200,speed_sps=5)
# some boards might require a different timer_id for each stepper:
#s1 = Stepper(18,19,steps_per_rev=200,speed_sps=50,timer_id=0)
#s2 = Stepper(20,21,steps_per_rev=200,speed_sps=50,timer_id=1)
EN1 = machine.Pin(0, machine.Pin.OUT, machine.Pin.PULL_UP) 
EN2 = machine.Pin(7, machine.Pin.OUT, machine.Pin.PULL_UP) 

s1.target_deg(90)
s2.target_deg(45)
time.sleep(5.0)
s1.target_deg(0)
s2.target_deg(5)
time.sleep(5.0)