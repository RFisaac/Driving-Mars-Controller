import time
from machine import UART
from motor_control import MotorController
from led_control import LEDController

# Initialize controllers
motors = MotorController()
leds = LEDController()

# Configure motor speed (500-2000, lower = faster)
motors.set_speed(1000)

# Set up LED colors for this specific rover
ROVER_COLOR = (0, 0, 255)  # Blue - change for different rovers
leds.set_base_color(ROVER_COLOR)
leds.set_brightness(0.5)

# UART setup
uart = UART(0, 9600)

def handle_command(cmd):
    """Handle incoming commands."""
    if cmd == b'forward\n':
        motors.forward(1.0)  # Move forward for 1 second
        leds.movement_forward()
    elif cmd == b'backward\n':
        motors.backward(1.0)
        leds.movement_backward()
    elif cmd == b'left\n':
        motors.turn_left(0.5)  # Turn for 0.5 seconds
        leds.movement_left()
    elif cmd == b'right\n':
        motors.turn_right(0.5)
        leds.movement_right()
    elif cmd == b'stop\n':
        motors.stop()

def main():
    last_pulse_update = time.ticks_ms()
    pulse_interval = 50  # Update pulse every 50ms
    
    while True:
        # Check for commands
        if uart.any():
            cmd = uart.readline()
            if cmd:
                handle_command(cmd)
        
        # Update LED pulse when not moving
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_pulse_update) >= pulse_interval:
            leds.update_pulse()
            last_pulse_update = current_time

if __name__ == '__main__':
    main()
