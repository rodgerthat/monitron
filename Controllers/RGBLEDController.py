# filename: RGBLEDController.py
# author: rodgerthat
# description: A Class to control an RGB LED
#   in this project, we're using it to create blue and red lights,
#   the two portions of the spectrum that stimulate photosynthesis the most

import os
import glob


class RGBLEDController:

    pin = ''

    # constructor
    # pass through the pin number
    def __init__(self, pin):
        self.pin = pin


#    def set_color:

#    def turn_on_rgbled:

#    def turn_off_rgbled:
