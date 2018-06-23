# filename: LampController.py
# author: rodgerthat
# description: A Class to control a 5V PC fan with a pull-down transistor

import RPi.GPIO as GPIO


class FanController:

    pin = ''

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

        GPIO.output(self.pin, GPIO.LOW)

    def turn_fan_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_fan_off(self):
        GPIO.output(self.pin, GPIO.LOW)
