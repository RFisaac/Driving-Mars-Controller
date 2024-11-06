import machine
from machine import Pin, Timer
import utime
 

EN = machine.Pin(0, machine.Pin.OUT, machine.Pin.PULL_UP) 
dir_pin = Pin(1, Pin.OUT)
step_pin = Pin(2, Pin.OUT)

EN2 = machine.Pin(7, machine.Pin.OUT, machine.Pin.PULL_UP) 
dir2_pin = Pin(6, Pin.OUT)
step2_pin = Pin(5, Pin.OUT)
steps_per_revolution = 200
 
# Initialize timer
tim = Timer()
 
def step(t):
    global step_pin
    step_pin.value(not step_pin.value())
    global step2_pin
    step2_pin.value(not step_pin.value())
 
def rotate_motor(delay):
    # Set up timer for stepping
    tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)
 
def loop():
    while True:
        # Set motor direction clockwise
        dir_pin.value(1)
        dir2_pin.value(1)

 
        # Spin motor slowly
        rotate_motor(2000)
        utime.sleep_ms(steps_per_revolution)
        tim.deinit()  # stop the timer
        utime.sleep(1)
 
        # Set motor direction counterclockwise
        dir_pin.value(0)
        dir2_pin.value(0)
 
        # Spin motor quickly
        rotate_motor(1000)
        utime.sleep_ms(steps_per_revolution)
        tim.deinit()  # stop the timer
        utime.sleep(1)
        print("loop")
 
if __name__ == '__main__':
    loop()