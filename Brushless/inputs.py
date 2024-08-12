import button
import pot
import encoder
import time

def main():
    button1 = button.Button(pin_number=18, name="Button1", reversed=True)
    button2 = button.Button(pin_number=19, name="Button2", reversed=False)
    toggle_switch = button.Button(pin_number=20, name="ToggleSwitch", reversed=True)
    
    throttle = pot.Pot(pin_number=26, name="Throttle")
    enc = encoder.Encoder(pin_a=4, pin_b=5)  # Initialize encoder

    while True:
        print(button1.read())
        print(button2.read())
        print(toggle_switch.read())
        print(throttle.read())  # Read and print potentiometer value
        enc.display_graphically()  # Display encoder value graphically
        time.sleep(0.1)

if __name__ == "__main__":
    main()
