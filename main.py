import time
from machine import UART, Pin
from motor_control import MotorController
from led_control import LEDController
from button_control import ButtonController
from rover_config import RoverConfig

# Initialize all controllers
motors = MotorController()
leds = LEDController()
button = ButtonController()
rover = RoverConfig()

# Configure motor speed (500-2000, lower = faster)
motors.set_speed(1000)

# Set initial LED configuration
leds.set_base_color(rover.current_color)
leds.set_brightness(0.5)

# UART setup
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

def handle_command(cmd_type):
    """Handle incoming commands."""
    if cmd_type == 'forward':
        motors.forward(1.0)
        leds.movement_forward()
    elif cmd_type == 'backward':
        motors.backward(1.0)
        leds.movement_backward()
    elif cmd_type == 'left':
        motors.turn_left(0.5)
        leds.movement_left()
    elif cmd_type == 'right':
        motors.turn_right(0.5)
        leds.movement_right()
    elif cmd_type == 'stop':
        motors.stop()
    elif cmd_type == 'on':
        # Handle initialization if needed
        pass

def handle_button_action(action):
    """Handle button actions."""
    if action == "click":
        # Reset/restart behavior
        print("Sending message")
        uart.write('Rover Message')
        motors.stop()
        leds.set_base_color(rover.current_color)
        
    elif action == "hold":
        # Change rover color/command set
        new_color = rover.next_color()
        print(f"Switching to {new_color} rover configuration")
        leds.set_base_color(rover.current_color)
        
        # Flash LEDs to indicate color change
        for _ in range(3):
            leds.set_brightness(0.1)
            time.sleep(0.1)
            leds.set_brightness(0.5)
            time.sleep(0.1)

def main():
    last_pulse_update = time.ticks_ms()
    pulse_interval = 50  # Update pulse every 50ms
    
    print(f"Rover started in {rover.colors[rover.current_color_index]} mode")
    
    while True:
        # Check for button actions
        button_action = button.check_button()
        if button_action:
            handle_button_action(button_action)
            continue
        
        # Check for commands
        if uart.any():
            cmd = uart.read(1)  # Read single character
            if cmd:
                # Convert bytes to string
                cmd_char = cmd.decode('utf-8')
                cmd_type = rover.get_command_type(cmd_char)
                if cmd_type:
                    print(f"Received command: {cmd_type}")
                    handle_command(cmd_type)
        
        # Update LED pulse when not moving
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_pulse_update) >= pulse_interval:
            leds.update_pulse()
            last_pulse_update = current_time

if __name__ == '__main__':
    main()