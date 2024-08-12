from machine import Pin

class Button:
    def __init__(self, pin_number, name, reversed=False):
        self.button = Pin(pin_number, Pin.IN, Pin.PULL_UP)  # Use PULL_UP based on your needs
        self.name = name
        self.reversed = reversed
    
    def is_pressed(self):
        state = self.button.value()
        return not state if self.reversed else state

    def read(self):
        if self.is_pressed():
            return f"{self.name}: Button is pressed"
        else:
            return f"{self.name}: Button is not pressed"

# Testing code (only runs if you execute button.py directly)
if __name__ == "__main__":
    test_button = Button(pin_number=19, name="TestButton", reversed=True)
    print(test_button.read())
