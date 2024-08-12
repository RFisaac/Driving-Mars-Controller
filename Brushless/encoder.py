import machine
import time

class Encoder:
    def __init__(self, pin_a, pin_b):
        self.pin_a = machine.Pin(pin_a, machine.Pin.IN, machine.Pin.PULL_UP)
        self.pin_b = machine.Pin(pin_b, machine.Pin.IN, machine.Pin.PULL_UP)
        self.enc_counter = 0
        self.qtr_cntr = 0
        self.error = 0
        self.last_enc_counter = 0
        self.enc_a_state_old = self.pin_a.value()
        self.enc_b_state_old = self.pin_b.value()

        # Setup interrupts
        self.pin_a.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=self.enc_handler)
        self.pin_b.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=self.enc_handler)

        # Debug print
        print("Encoder initialized with pins:", pin_a, pin_b)

    def enc_handler(self, source):
        enc_a_state = self.pin_a.value()
        enc_b_state = self.pin_b.value()

        if enc_a_state == self.enc_a_state_old and enc_b_state == self.enc_b_state_old:
            self.error += 1
            print(f"Debug: Error incremented, current error count: {self.error}")
        elif (enc_a_state == 1 and self.enc_b_state_old == 0) or (enc_a_state == 0 and self.enc_b_state_old == 1):
            self.enc_counter += 1
            self.qtr_cntr = round(self.enc_counter / 4)
            print(f"Debug: Clockwise rotation detected, encoder count: {self.enc_counter}")
        elif (enc_a_state == 1 and self.enc_b_state_old == 1) or (enc_a_state == 0 and self.enc_b_state_old == 0):
            self.enc_counter -= 1
            self.qtr_cntr = round(self.enc_counter / 4)
            print(f"Debug: Counter-clockwise rotation detected, encoder count: {self.enc_counter}")
        else:
            self.error += 1
            print(f"Debug: Unrecognized state, error count: {self.error}")

        self.enc_a_state_old = enc_a_state
        self.enc_b_state_old = enc_b_state

    def display_graphically(self, max_steps=600):
        degrees = (self.qtr_cntr % max_steps) * (360 / max_steps)
        num_chars = int(degrees / (360 / 40))
        pie_chart = '[' + '#' * num_chars + ' ' * (40 - num_chars) + ']'
        print(f"\rDegrees: {degrees:.2f} {pie_chart}", end='')

    def get_qtr_cntr(self):
        return self.qtr_cntr

# Main program loop for testing
if __name__ == "__main__":
    encoder = Encoder(pin_a=4, pin_b=5)
    while True:
        time.sleep(0.2)
        if encoder.get_qtr_cntr() != encoder.last_enc_counter:
            encoder.last_enc_counter = encoder.get_qtr_cntr()
            encoder.display_graphically()
