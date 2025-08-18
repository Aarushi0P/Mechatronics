class Sensor:
    def __init__(self, trig_pin=21, echo_pin=20, piezo_pin=1):
        self.trigger = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.piezo = Pin(piezo_pin, Pin.IN)
    def get_distance(self):
        self.trigger.low
        utime.sleep(0.01)
        self.trigger.high(0.000005)
        self.trigger.low()
    while self.echo.value() == 0:
        signaloff = utime.ticks_us()
    while self.echo.value()==1:
        signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        return distance
    def is_vibrating(self):
        return self.piezo.value() == 1

sensor_module = SensorModule()

while True:
    distance = sensor_module.get_distance()
    vibration = sensor_module.is_vibrating()

    print("Distance:", distance, "cm")
    print("Vibration detected!" if vibration else "No vibration.")
    utime.sleep(0.5)
