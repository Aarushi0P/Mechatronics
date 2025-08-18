from machine import Pin
import time

# Connect DO to GP15
piezo_digital = Pin(7, Pin.IN)

while True:
    if piezo_digital.value() == 1:
        print("Vibration detected!")
    else:
        print("No vibration.")
    time.sleep(0.07)
