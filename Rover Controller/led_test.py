
import led_control

    
while True:
    led_control.set_led_color((0, 255, 0))  # Set both strips to green
    print("set color")
    led_control.leds_forwards()  # Run forwards animation
    print("forward")
    led_control.slow_pulse_leds()
    print("slow pulse")
    