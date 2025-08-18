from motor_module import MotorController
from sensor_module import UltrasonicSensor, PiezoSensor
from button import Button
import random
import time


class Pet:
    def __init__(self):
        self.motor = MotorController()
        self.ultrasonicsensor = UltrasonicSensor()
        self.piezosensor = PiezoSensor()
    def on_off(status, location, speed):
        button.check_status()
        if status = True:
            self.