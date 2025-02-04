import neopixel
import machine
import time

class LEDController:
    def __init__(self, left_pin=14, right_pin=15, num_leds=16):
        # Initialize the LED strips
        self.num_leds = num_leds
        self.left_strip = neopixel.NeoPixel(machine.Pin(left_pin), num_leds)
        self.right_strip = neopixel.NeoPixel(machine.Pin(right_pin), num_leds)
        
        # State variables
        self.brightness = 0.5
        self.base_color = (0, 0, 255)  # Default blue
        self.movement_color = (255, 255, 255)  # White for movement
        self.is_moving = False
        self.current_pulse_level = 0
        self.pulse_direction = 1
        
    def set_base_color(self, color):
        """Set the base color for the idle pulse."""
        self.base_color = color
        
    def set_movement_color(self, color):
        """Set the color used for movement animations."""
        self.movement_color = color
        
    def set_brightness(self, level):
        """Set the overall brightness (0.0 to 1.0)."""
        self.brightness = max(0.0, min(1.0, level))
        
    def _scale_color(self, color, additional_scale=1.0):
        """Scale a color by brightness and optional additional scaling."""
        r, g, b = color
        factor = self.brightness * additional_scale
        return (int(r * factor), int(g * factor), int(b * factor))
    
    def _set_all_leds(self, left_colors, right_colors):
        """Set all LEDs with different colors for each strip."""
        for i in range(self.num_leds):
            self.left_strip[i] = left_colors[i] if isinstance(left_colors, list) else left_colors
            self.right_strip[i] = right_colors[i] if isinstance(right_colors, list) else right_colors
        self.left_strip.write()
        self.right_strip.write()
        
    def update_pulse(self):
        """Update the background pulse animation."""
        if not self.is_moving:
            # Update pulse level
            self.current_pulse_level += self.pulse_direction * 0.05
            if self.current_pulse_level >= 1.0:
                self.current_pulse_level = 1.0
                self.pulse_direction = -1
            elif self.current_pulse_level <= 0.2:
                self.current_pulse_level = 0.2
                self.pulse_direction = 1
                
            # Apply the pulse
            color = self._scale_color(self.base_color, self.current_pulse_level)
            self._set_all_leds(color, color)
            
    def movement_forward(self):
        """Animation for forward movement."""
        self.is_moving = True
        for i in range(self.num_leds):
            colors = [(0,0,0)] * self.num_leds
            colors[i] = self._scale_color(self.movement_color)
            self._set_all_leds(colors, colors)
            time.sleep(0.05)
        self.is_moving = False
            
    def movement_backward(self):
        """Animation for backward movement."""
        self.is_moving = True
        for i in range(self.num_leds - 1, -1, -1):
            colors = [(0,0,0)] * self.num_leds
            colors[i] = self._scale_color(self.movement_color)
            self._set_all_leds(colors, colors)
            time.sleep(0.05)
        self.is_moving = False
            
    def movement_left(self):
        """Animation for left turn."""
        self.is_moving = True
        for i in range(self.num_leds):
            left_colors = [(0,0,0)] * self.num_leds
            right_colors = [(0,0,0)] * self.num_leds
            left_colors[self.num_leds - 1 - i] = self._scale_color(self.movement_color)
            right_colors[i] = self._scale_color(self.movement_color)
            self._set_all_leds(left_colors, right_colors)
            time.sleep(0.05)
        self.is_moving = False
            
    def movement_right(self):
        """Animation for right turn."""
        self.is_moving = True
        for i in range(self.num_leds):
            left_colors = [(0,0,0)] * self.num_leds
            right_colors = [(0,0,0)] * self.num_leds
            left_colors[i] = self._scale_color(self.movement_color)
            right_colors[self.num_leds - 1 - i] = self._scale_color(self.movement_color)
            self._set_all_leds(left_colors, right_colors)
            time.sleep(0.05)
        self.is_moving = False
