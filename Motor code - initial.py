from machine import Pin
import utime

class StepperMotor:
    def __init__(self, pin_numbers, step_sequence, delay=0.02):
        self.pins = [Pin(pin, Pin.OUT) for pin in pin_numbers]
        self.sequence = step_sequence
        self.delay = delay
        self.step_count = len(step_sequence)
        self.current_step = 0

    def step_forward(self, steps=1):
        for _ in range(steps):
            self._apply_step(self.current_step)
            self.current_step = (self.current_step + 1) % self.step_count
            utime.sleep(self.delay)

    def step_backward(self, steps=1):
        for _ in range(steps):
            self._apply_step(self.current_step)
            self.current_step = (self.current_step - 1) % self.step_count
            utime.sleep(self.delay)

    def _apply_step(self, step_index):
        step = self.sequence[step_index]
        for i in range(4):
            self.pins[i].value(step[i])

    def release(self):
        for pin in self.pins:
            pin.value(0)