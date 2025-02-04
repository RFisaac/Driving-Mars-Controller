from machine import Pin
from time import sleep

class MotorController:
    def __init__(self):
        # Left motor pins with proper pull-up/down
        self.pSTEP_L = Pin(2, Pin.OUT, Pin.PULL_DOWN)
        self.pDIR_L = Pin(1, Pin.OUT, Pin.PULL_DOWN)
        self.pEN_L = Pin(0, Pin.OUT, Pin.PULL_UP)
        self.FAULT_L = Pin(3, Pin.IN, Pin.PULL_UP)
        
        # Right motor pins with proper pull-up/down
        self.pSTEP_R = Pin(5, Pin.OUT, Pin.PULL_DOWN)
        self.pDIR_R = Pin(6, Pin.OUT, Pin.PULL_DOWN)
        self.pEN_R = Pin(7, Pin.OUT, Pin.PULL_UP)
        self.FAULT_R = Pin(4, Pin.IN, Pin.PULL_UP)
        
        # Reset pin
        self.RST = Pin(16, Pin.IN, Pin.PULL_UP)
        
        # Timing constants
        self.uS = 0.000001  # one microsecond
        self.usDelay = 1000  # microseconds between steps (adjustable)
        
        # Initialize motors
        self._initialize_motors()
        
    def _initialize_motors(self):
        """Initialize motors to a safe state without movement"""
        # Start with motors disabled
        self.pEN_L.value(1)
        self.pEN_R.value(1)
        
        # Set initial directions
        self.pDIR_L.value(0)
        self.pDIR_R.value(0)
        
        # Ensure step pins are low
        self.pSTEP_L.value(0)
        self.pSTEP_R.value(0)
        
        print("Motors initialized in safe state")
        
    def set_speed(self, delay):
        """Set step delay in microseconds (500-2000). Lower = faster."""
        self.usDelay = max(500, min(2000, delay))
        
    def _step_motors(self, left_dir, right_dir, steps, duration=None):
        """Step both motors using microsecond timing"""
        # Set directions
        self.pDIR_L.value(not left_dir)
        self.pDIR_R.value(right_dir)
        
        # Enable motors
        self.pEN_L.value(0)
        self.pEN_R.value(0)
        
        # If duration provided, calculate steps
        if duration:
            steps = int((duration * 1000000) / (self.usDelay * 2))
        
        # Step both motors with microsecond timing
        for _ in range(steps):
            self.pSTEP_L.value(1)
            self.pSTEP_R.value(1)
            sleep(self.uS * self.usDelay)
            self.pSTEP_L.value(0)
            self.pSTEP_R.value(0)
            sleep(self.uS * self.usDelay)
            
        # Disable motors
        self.pEN_L.value(1)
        self.pEN_R.value(1)
        
    def forward(self, duration=1.0):
        """Move forward for specified duration in seconds."""
        self._step_motors(True, True, None, duration)
        
    def backward(self, duration=1.0):
        """Move backward for specified duration in seconds."""
        self._step_motors(False, False, None, duration)
        
    def turn_left(self, duration=1.0):
        """Turn left for specified duration in seconds."""
        self._step_motors(False, True, None, duration)
        
    def turn_right(self, duration=1.0):
        """Turn right for specified duration in seconds."""
        self._step_motors(True, False, None, duration)
        
    def stop(self):
        """Stop both motors."""
        self.pEN_L.value(1)
        self.pEN_R.value(1)