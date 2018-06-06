############################################
# filename: RGBLEDController.py
# author: rodgerthat
# description: class to control RGB LED
############################################

import RPi.GPIO as GPIO


class RGBLEDController:

    # assign GPIO pin numbers to variables
    # 11 = GPIO17
    # 13 = GPIO27
    # 15 = GPIO22

    # default pin values
    redPin = 11
    greenPin = 13
    bluePin = 15

    redIsOn = False
    greenIsOn = False
    blueIsOn = False

    def __init__(self, red_pin, green_pin, blue_pin):
        self.redPin = red_pin
        self.greenPin = green_pin
        self.bluePin = blue_pin

        pass

    ################################
    # LED Control Methods
    ##############################

    def blink(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def turn_off(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    ################################
    # LED Toggle Methods
    ##############################

    def toggle_red(self):

        if not self.redIsOn:
            self.red_on()
            self.redIsOn = True
        else:
            self.red_off()
            self.redIsOn = False

    def toggle_green(self):

        if not self.greenIsOn:
            self.green_on()
            self.greenIsOn = True
        else:
            self.green_off()
            self.greenIsOn = False

    def toggle_blue(self):

        if not self.blueIsOn:
            self.blue_on()
            self.blueIsOn = True
        else:
            self.blue_off()
            self.blueIsOn = False

    #######################
    # ON
    #######################

    def red_on(self):
        self.blink(self.redPin)

    def green_on(self):
        self.blink(self.greenPin)

    def blue_on(self):
        self.blink(self.bluePin)

    def yellow_on(self):
        self.blink(self.redPin)
        self.blink(self.greenPin)

    def cyan_on(self):
        self.blink(self.greenPin)
        self.blink(self.bluePin)

    def magenta_on(self):
        self.blink(self.redPin)
        self.blink(self.bluePin)

    def white_on(self):
        self.blink(self.redPin)
        self.blink(self.greenPin)
        self.blink(self.bluePin)

    #######################
    # OFF
    #######################

    def red_off(self):
        self.turn_off(self.redPin)

    def green_off(self):
        self.turn_off(self.greenPin)

    def blue_off(self):
        self.turn_off(self.bluePin)

    def yellow_off(self):
        self.turn_off(self.redPin)
        self.turn_off(self.greenPin)

    def cyan_off(self):
        self.turn_off(self.greenPin)
        self.turn_off(self.bluePin)

    def magenta_off(self):
        self.turn_off(self.redPin)
        self.turn_off(self.bluePin)

    def white_off(self):
        self.turn_off(self.redPin)
        self.turn_off(self.greenPin)
        self.turn_off(self.bluePin)
