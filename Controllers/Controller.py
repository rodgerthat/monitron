# filename: Controller.py
# author: rodgerthat
# description: A Base Class to extend various controllers from

import RPi.GPIO as GPIO


class Controller:

    pin = ''
    is_on = False   # a flag to check if on or off

    def __init__(self, pin):

        self.pin = pin
        # set the pin to an output pin
        GPIO.setup(self.pin, GPIO.OUT)

        # set the output voltage to LOW or 0
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):

        # set the output pin voltage to 3.3V
        if not self.is_on:
            GPIO.output(self.pin, GPIO.HIGH)
            self.is_on = True

    def turn_off(self):

        # set the output pin voltage to 0
        if self.is_on:
            GPIO.output(self.pin, GPIO.LOW)
            self.is_on = False

