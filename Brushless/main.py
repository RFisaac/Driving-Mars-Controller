import machine
import time
import gamepad

# Initialize the gamepad
gamepad = Gamepad()

# Configure the buttons and analog input
button1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
toggle_switch = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
pot = machine.ADC(26)

def read_buttons():
    return {
        "button1": not button1.value(),  # Assuming active-low configuration
        "button2": not button2.value(),
        "toggle_switch": not toggle_switch.value()
    }

def read_pot():
    return pot.read_u16()  # Read the ADC value (0-65535)

def normalize(value, min_in, max_in, min_out, max_out):
    return (value - min_in) / (max_in - min_in) * (max_out - min_out) + min_out

def main():
    while True:
        buttons = read_buttons()
        pot_value = read_pot()
        
        # Create a bitmask for button states
        button_states = 0
        if buttons["button1"]:
            button_states |= 0x01
        if buttons["button2"]:
            button_states |= 0x02
        if buttons["toggle_switch"]:
            button_states |= 0x04
        
        # Update the gamepad state
        x_value = normalize(pot_value, 0, 65535, -127, 127)  # Normalize for HID range
        y_value = 0  # Example fixed value, update with actual data if needed

        gamepad.send_report(button_states, int(x_value), int(y_value))
        
        time.sleep(0.01)  # Adjust the delay as needed

if __name__ == "__main__":
    main()
