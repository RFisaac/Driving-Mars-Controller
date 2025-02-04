import machine
import time

# Configuration
BUTTON_PIN = 10         # GPIO pin where the button is connected
LED_PIN = 25            # Onboard LED pin (GPIO 25)

# Initialize the button with PULL_UP and LED pins
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Variable to track the state of the LED
led_state = False

# Debounce time (to avoid multiple toggles from a single press)
debounce_time = 0.2  # seconds

# Main loop
while True:
    if button.value() == 0:  # Button pressed (reads LOW)
        led_state = not led_state  # Toggle LED state
        led.value(led_state)  # Update the onboard LED

        # Print the current state of the LED
        if led_state:
            print("LED is ON")
        else:
            print("LED is OFF")

        time.sleep(debounce_time)  # Debounce delay to avoid double toggling
