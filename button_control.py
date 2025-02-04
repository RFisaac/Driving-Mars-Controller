from machine import Pin
import time

class ButtonController:
    def __init__(self, pin=10):
        self.button = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.last_press_time = 0
        self.hold_duration = 1.0  # seconds to consider a "hold"
        self.debounce_time = 0.05  # 50ms debounce
        
    def check_button(self):
        """
        Check button state and return action type.
        Returns: 
            None: No action
            "click": Short press detected
            "hold": Long press detected
        """
        if self.button.value() == 0:  # Button is pressed (active low)
            press_start = time.time()
            
            # Wait for button release or hold duration
            while self.button.value() == 0:
                if time.time() - press_start >= self.hold_duration:
                    # Wait for release before returning
                    while self.button.value() == 0:
                        time.sleep(0.01)
                    return "hold"
                time.sleep(0.01)
            
            # Check if this is a new press (debounce)
            if time.time() - self.last_press_time > self.debounce_time:
                self.last_press_time = time.time()
                return "click"
                
        return None