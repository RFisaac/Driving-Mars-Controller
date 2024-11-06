import machine
import time
from machine import Pin


led = Pin(25, Pin.OUT)
# Motor 1 Pin Setup
EN1 = machine.Pin(0, machine.Pin.OUT, machine.Pin.PULL_UP)   # Enable motor driver 1 (pull-up)
DIR1 = machine.Pin(1, machine.Pin.OUT, machine.Pin.PULL_DOWN) # Direction pin (pull-down for a default state)
STEP1 = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_DOWN) # Step pin (pull-down for a default state)
FAULT1 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)  # Fault pin with pull-up
RST = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# Motor 2 Pin Setup
EN2 = machine.Pin(7, machine.Pin.OUT, machine.Pin.PULL_UP)    # Enable motor driver 2 (pull-up)
DIR2 = machine.Pin(6, machine.Pin.OUT, machine.Pin.PULL_DOWN) # Direction pin (pull-down for a default state)
STEP2 = machine.Pin(5, machine.Pin.OUT, machine.Pin.PULL_DOWN) # Step pin (pull-down for a default state)
FAULT2 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Fault pin with pull-up

# Helper function to step motor
def step_motor(step_pin, steps, delay=0.05):
    for _ in range(steps):
        step_pin.value(1)
        time.sleep(delay)
        step_pin.value(0)
        time.sleep(delay)

# Main loop
while True:
    # Check for faults
    if FAULT1.value() == 0:
        print("FAULT on motor 1!")
        time.sleep(0.05)
    else:
        print("Motor 1 is OK")
        time.sleep(0.05)

    if FAULT2.value() == 0:
        print("FAULT on motor 2!")
        time.sleep(0.05)
    else:
        print("Motor 2 is OK")
        time.sleep(0.05)
    
    # Enable both drivers
    EN1.value(0)  # Enable motor 1 (Low = enabled)
    print("Motor 1 enabled")
    time.sleep(0.05)
    EN2.value(0)  # Enable motor 2 (Low = enabled)
    print("Motor 2 enabled")
    time.sleep(0.05)

    # Set motor directions
    DIR1.value(1)  # Set direction for motor 1 (1 = clockwise)
    print("Motor 1 direction set")
    time.sleep(0.05)
    DIR2.value(0)  # Set direction for motor 2 (0 = counter-clockwise)
    print("Motor 2 direction set")
    time.sleep(0.05)

    # Step both motors
    step_motor(STEP1, 200)  # Step motor 1 200 steps
    print("Motor 1 200 steps")
    time.sleep(0.05)
    step_motor(STEP2, 200)  # Step motor 2 200 steps
    print("Motor 2 200 steps")
    # Pause between steps
    time.sleep(0.05)
    
    # Disable motors after stepping
    EN1.value(0.05)  # Disable motor 1 (High = disabled)
    print("Motor 1 disabled")
    time.sleep(0.05)
    EN2.value(0.05)  # Disable motor 2 (High = disabled)
    print("Motor 2 disabled")
    time.sleep(0.05)

    time.sleep(2)  # Pause before the next loop
    print("! LOOP !")
    led.toggle()
