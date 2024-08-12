from machine import ADC
import time

class Pot:
    def __init__(self, pin_number, name):
        self.pot = ADC(pin_number)
        self.name = name
    
    def read(self):
        value = self.pot.read_u16()  # Read the ADC value (0 to 65535)
        return f"{self.name}: {value}"

# Add this block to test the Potentiometer class independently
if __name__ == "__main__":
    test_pot = Pot(pin_number=26, name="Throttle")
    while True:
        print(test_pot.read())
        time.sleep(0.1)
