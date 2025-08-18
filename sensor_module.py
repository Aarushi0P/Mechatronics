from machine import Pin
import utime

class PiezoSensor: 
    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)

    def detect_vibration(self):
        return self.pin.value() == 1
    

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        utime.sleep(1)  # Allow sensor to settle

    def get_distance(self):
        self.trigger.low()
        utime.sleep(0.001)
        self.trigger.high()
        utime.sleep_us(10)
        self.trigger.low()

        # Wait for echo high
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()

        # Wait for echo low
        while self.echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        return round(distance, 2)
