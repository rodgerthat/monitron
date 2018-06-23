# filename: Controller.py
# author: rodgerthat
# description: A Base Class to extend various controllers from

import RPi.GPIO as GPIO


class Controller:

    pin = ''

    def __init__(self, pin):

        self.pin = pin
        # set the pin to an output pin
        GPIO.setup(self.pin, GPIO.OUT)

        # set the output voltage to LOW or 0
        GPIO.output(self.pin, GPIO.LOW)

    def turn_pin_on(self):

        # set the output pin voltage to 3.3V
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_pin_off(self):

        # set the output pin voltage to 0
        GPIO.output(self.pin, GPIO.LOW)
