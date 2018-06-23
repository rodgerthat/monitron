# filename: OutletBoxController.py
# author: rodgerthat
# description: A Class to control an 8 Socket 120V outlet box

import RPi.GPIO as GPIO
from Controllers.Controller import Controller


class OutletBoxController(Controller):

    bcm_pin_dict = {
        1: 9,
        2: 10,
        3: 22,
        4: 27,
        5: 17,
        6: 4,
        7: 3,
        8: 2,
    }

    board_gpio_pin_dict = {
        1: 21,
        2: 19,
        3: 15,
        4: 13,
        5: 11,
        6: 7,
        7: 5,
        8: 3
    }

    def turn_outlet_on(self, outlet_number):

        pin = self.bcm_pin_dict[outlet_number]
        GPIO.output(pin, GPIO.HIGH)

    def turn_outlet_off(self, outlet_number):

        pin = self.bcm_pin_dict[outlet_number]
        GPIO.output(pin, GPIO.LOW)
