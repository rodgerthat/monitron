#

import RPi.GPIO as GPIO


class HeatController:

    heatON = True   # Heater is plugged into 'Normally ON' outlet in IoT Relay
                    # this is so if there's any kind of reset or power outage it will
                    # come on by default

    outletType = 'NormallyON'

    def __init__(self, outlet_type):

        self.outletType = outlet_type

        # prime the device!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)

        if self.outletType == 'NormallyON':
            GPIO.output(18, GPIO.HIGH)   # the IoT relay initially starts in the OFF position

        elif self.outletType == 'NormallyOFF':
            GPIO.output(18, GPIO.LOW)   # the IoT relay initially starts in the OFF position

    def turn_ON(self):

        # turn on the HEAT
        if self.outletType == 'NormallyON':
            GPIO.output(18, GPIO.LOW)

        elif self.outletType == 'NormallyOFF':
            GPIO.output(18, GPIO.HIGH)

        self.heatON = True

    def turn_OFF(self):

        # turn off the HEAT (brow brow kiddies!)
        if self.outletType == 'NormallyON':
            GPIO.output(18, GPIO.HIGH)

        if self.outletType == 'NormallyOFF':
            GPIO.output(18, GPIO.LOW)

        self.heatON = False
