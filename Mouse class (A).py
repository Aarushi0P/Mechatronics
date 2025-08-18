from motor_module import StepperMotor
from sensor_module import UltrasonicSensor
from sensor_module import PiezoSensor
from machine import Pin
import time

class Mouse: 
    def __init__(self):
        step_seq = [
            [1, 0, 0, 1], #each list represents which coils get power at a given step
            [1, 0, 0, 0],# 1 = energise 0= turn off 
            [1, 1, 0, 0],#8 step sequence to achieve half step pattern
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
        ] 
        self.motor = StepperMotor([5, 6, 7, 8], step_seq)
        self.ultrasonic = UltrasonicSensor(trigger_pin = 4, echo_pin = 3) 
        self.piezo = PiezoSensor(pin_number = 15)
    def run(self):
        while True:
            
            dist = self.ultrasonic.get_distance()
            vibration = self.piezo.detect_vibration()
            print(f"Distance: {dist} cm, Vibration: {vibration}") # checkpoint 
            if vibration:
                print("Vibration detected! Stopping motor") # Checkpoint piezo
            elif dist == 10: 
                print("Obstacle! Reversing")
                self.motor.step_backward(50)
            else:
                print("Clear")
                self.motor.step_forward(50)
            time.sleep(0.1)
#instance yay!
while True:
    pet_kitty = Mouse()
    pet_kitty.run()        
