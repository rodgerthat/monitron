"""
 " ;FileName: OutletBox
 " ;Author: goat
 " ;Created: 6/23/18
 " ;Description: A Class for interfacing with the outlet box
    " created using this online tutorial:
    " ;URL: http://www.instructables.com/id/Web-Controlled-8-Channel-Powerstrip/
 """

import RPi.GPIO as GPIO
from Controllers.Controller import Controller


class OutletBoxController(Controller):
    """
    ;property: outlet_number: the number of the outlet you want to manipulate
    ;property: pin_map_key: the string key to reference the correct pin mapping pairs
    ;property: pin_maps: a dictionary of different pin mappings of the outlet numbers to output pins.
    """
    outlet_number = 0
    pin_map_key = ""
    is_on = False       # this is a flag to not trigger the relay needlessly

    pin_maps = {

        "bcm_pin_dict": {
            1: 9,
            2: 10,
            3: 22,
            4: 27,
            5: 17,
            6: 4,
            7: 3,
            8: 2,
        },

        "board_gpio_pin_dict":  {
            1: 21,
            2: 19,
            3: 15,
            4: 13,
            5: 11,
            6: 7,
            7: 5,
            8: 3
        }
    }

    def __init__(self, outlet_number, pin_map_key):
        
        self.outlet_number = outlet_number
        self.pin_map_key = pin_map_key

    def set_pins(self):
        # set each pin as an output pin, and set it's initial value to HIGH
        # this is because of how the relays are wired, when you set the pin to HIGH
        # the relay disconnects the corresponding 120V outlet

        # print(self.pin_map_key)
        # print(self.outlet_number)

        for index, pin in self.pin_maps[self.pin_map_key].items():

            # print(index, pin)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def turn_outlet_on(self):

        # if it's not already on, then turn it on
        if not self.is_on:
            pin = self.pin_maps[self.pin_map_key][self.outlet_number]
            GPIO.output(pin, GPIO.HIGH)

    def turn_outlet_off(self):

        # if the item is on, it off
        if self.is_on:
            pin = self.pin_maps[self.pin_map_key][self.outlet_number]
            GPIO.output(pin, GPIO.LOW)
