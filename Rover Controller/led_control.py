import neopixel
import machine
import time

# Configuration for two LED strips
LEFT_LED_PIN = 14  # GPIO pin for left-side LEDs
RIGHT_LED_PIN = 15  # GPIO pin for right-side LEDs
NUM_LEDS = 16  # Number of LEDs per strip

# Initialize the two LED strips
left_strip = neopixel.NeoPixel(machine.Pin(LEFT_LED_PIN), NUM_LEDS)
right_strip = neopixel.NeoPixel(machine.Pin(RIGHT_LED_PIN), NUM_LEDS)

# Global variables
current_color = (255, 255, 255)  # Default color: White
brightness = 0.5  # Brightness level (0.0 to 1.0)

# Utility functions
def scale_color(color):
    r, g, b = color
    return (int(r * brightness), int(g * brightness), int(b * brightness))

def set_all_leds(strip, color):
    """Set all LEDs on a given strip to the specified color."""
    scaled_color = scale_color(color)
    for i in range(NUM_LEDS):
        strip[i] = scaled_color
    strip.write()

def set_brightness(level):
    """Adjust the brightness level (0.0 to 1.0)."""
    global brightness
    brightness = max(0.0, min(level, 1.0))

def set_led_color(color):
    """Set both LED strips to the same color."""
    global current_color
    current_color = color
    set_all_leds(left_strip, color)
    set_all_leds(right_strip, color)

# LED animations
def slow_pulse_leds():
    """Slow pulse animation on both strips."""
    while True:
        for i in range(0, 256, 5):
            set_all_leds(left_strip, (i, i, i))
            set_all_leds(right_strip, (i, i, i))
            time.sleep(0.02)
        for i in range(255, -1, -5):
            set_all_leds(left_strip, (i, i, i))
            set_all_leds(right_strip, (i, i, i))
            time.sleep(0.02)

def leds_forwards():
    """Chasing pattern forwards on both strips."""
    for i in range(NUM_LEDS):
        set_all_leds(left_strip, (0, 0, 0))
        set_all_leds(right_strip, (0, 0, 0))
        left_strip[i] = scale_color(current_color)
        right_strip[i] = scale_color(current_color)
        left_strip.write()
        right_strip.write()
        time.sleep(0.05)

def leds_backwards():
    """Chasing pattern backwards on both strips."""
    for i in range(NUM_LEDS - 1, -1, -1):
        set_all_leds(left_strip, (0, 0, 0))
        set_all_leds(right_strip, (0, 0, 0))
        left_strip[i] = scale_color(current_color)
        right_strip[i] = scale_color(current_color)
        left_strip.write()
        right_strip.write()
        time.sleep(0.05)

def leds_left():
    """Chasing back on left strip, forward on right strip."""
    for i in range(NUM_LEDS):
        set_all_leds(left_strip, (0, 0, 0))
        set_all_leds(right_strip, (0, 0, 0))
        left_strip[NUM_LEDS - 1 - i] = scale_color(current_color)
        right_strip[i] = scale_color(current_color)
        left_strip.write()
        right_strip.write()
        time.sleep(0.05)

def leds_right():
    """Chasing back on right strip, forward on left strip."""
    for i in range(NUM_LEDS):
        set_all_leds(left_strip, (0, 0, 0))
        set_all_leds(right_strip, (0, 0, 0))
        left_strip[i] = scale_color(current_color)
        right_strip[NUM_LEDS - 1 - i] = scale_color(current_color)
        left_strip.write()
        right_strip.write()
        time.sleep(0.05)

def leds_stop():
    """Turn off both LED strips."""
    set_all_leds(left_strip, (0, 0, 0))
    set_all_leds(right_strip, (0, 0, 0))

def loading_bar(percent):
    """Display a loading bar up to a percentage on both strips."""
    leds_to_light = int(NUM_LEDS * percent / 100)
    set_all_leds(left_strip, (0, 0, 0))
    set_all_leds(right_strip, (0, 0, 0))
    for i in range(leds_to_light):
        left_strip[i] = scale_color((255, 255, 255))
        right_strip[i] = scale_color((255, 255, 255))
    left_strip.write()
    right_strip.write()
