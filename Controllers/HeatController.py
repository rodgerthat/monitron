

import RPi.GPIO as GPIO


class HeatController():

    heatON = False

    def __init__(self):

        # prime the device!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        heatON = False;

    def turn_ON(self):

        # turn on the HEAT
        GPIO.output(18, GPIO.HIGH)
        heatON = True

    def turn_OFF(self):

        # turn off the HEAT (brow brow kiddies!)
        GPIO.output(18, GPIO.LOW)
        heatON = False



