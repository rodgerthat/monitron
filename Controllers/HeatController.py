

import RPi.GPIO as GPIO


class HeatController():

    heatON = True   # Heater is plugged into 'Normally ON' outlet in IoT Relay
                    # this is so if there's any kind of reset or power outage it will
                    # come on by default

    def __init__(self):

        # prime the device!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.LOW)   # the IoT relay initially starts in the OFF position
        self.heatON = False;

    def turn_ON(self):

        # turn on the HEAT
        GPIO.output(18, GPIO.HIGH)
        self.heatON = True

    def turn_OFF(self):

        # turn off the HEAT (brow brow kiddies!)
        GPIO.output(18, GPIO.LOW)
        self.heatON = False



