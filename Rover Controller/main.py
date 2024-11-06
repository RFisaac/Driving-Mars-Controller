# === Imports ===
import machine
import time
import led_control  # Import your LED control module

# Example UART Configuration
UART_BAUDRATE = 9600
uart = machine.UART(0, baudrate=UART_BAUDRATE)

# Battery Configuration
BATTERY_PIN = 26  # ADC pin for battery voltage
adc = machine.ADC(machine.Pin(BATTERY_PIN))
low_battery_threshold = 12.0

def read_battery_voltage():
    """Read and return the battery voltage."""
    return adc.read_u16() * (3.3 / 65535) * 6.085  # Adjust for voltage divider

def listen_for_uart_command():
    """Listen for UART commands and return them."""
    if uart.any():
        return uart.readline().decode().strip()
    return None

def handle_uart_command(command):
    """Handle the received UART command."""
    if command == "forwards":
        led_control.leds_forwards()
    elif command == "backwards":
        led_control.leds_backwards()
    elif command == "left":
        led_control.leds_left()
    elif command == "right":
        led_control.leds_right()
    elif command == "stop":
        led_control.leds_stop()
    elif command.startswith("set_color"):
        _, r, g, b = command.split()
        led_control.set_led_color((int(r), int(g), int(b)))
    elif command.startswith("set_brightness"):
        _, level = command.split()
        led_control.set_brightness(float(level))

def main_loop():
    """Main program loop."""
    while True:
        # Check battery voltage
        voltage = read_battery_voltage()
        if voltage < low_battery_threshold:
            led_control.leds_stop()  # Stop if battery is low
            print("Low battery! Voltage:", voltage)
            continue  # Skip the rest of the loop

        # Listen for UART command
        command = listen_for_uart_command()
        if command:
            print("Received command:", command)
            handle_uart_command(command)
        else:
            # Run idle animation if no command received
            led_control.slow_pulse_leds()

def setup():
    """Setup the system and start the main loop."""
    print("Starting setup...")
    led_control.loading_bar(25)
    time.sleep(0.5)

    led_control.set_led_color((255, 255, 255))  # Set initial color to white
    led_control.set_brightness(0.5)  # Set initial brightness

    voltage = read_battery_voltage()
    print("Battery Voltage:", voltage)
    if voltage < low_battery_threshold:
        print("Battery too low. Stopping.")
        led_control.leds_stop()
        return  # Stop setup if battery is low

    led_control.loading_bar(75)
    time.sleep(0.5)

    uart.write("on\n")  # Send UART on signal
    print("Sent UART on signal.")

    led_control.loading_bar(100)
    time.sleep(0.5)

    print("Setup complete. Entering main loop.")
    main_loop()

# Start the program
setup()
