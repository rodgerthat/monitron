#!/usr/bin/env python2
#
# filename: Monitron.py
# author: rodgerthat
# description:
#   monitors shed 1,

import time

# TODO : you're using aliases now, come back and clean up all the 'self' references.
# since the class technically doesn't need to have the getters and setters as object properties.

#from Getters.TempGetter import TempGetter as TempGetter
from Getters.TemperatureAndHumidityGetter import TemperatureAndHumidityGetter as TemperatureAndHumidityGetter
from Getters.TimeGetter import TimeGetter as TimeGetter
from Setters.DataStorer import DataStorer as DataStorer
from Controllers.Controller import Controller as Controller
from Controllers.HeatController import HeatController as HeatController
from Controllers.FanController import FanController as FanController
from Controllers.RGBLEDController import RGBLEDController as RGBLEDController
from Controllers.OutletBoxController import OutletBoxController as OutletBoxController


class Monitron:

    pin_map_key = "bcm_pin_dict"
    currentTemperature = 0.0
    currentHumidity = 0.0

    # tempGetter = object
    temperatureAndHumidityGetter = object

    dataStorer = object

    # heatController = object

    humidityController = object
    fanController = object

    rgb_led_1 = object
    rgb_led_2 = object
    rgb_led_3 = object
    rgb_led_4 = object

    outletBoxController = object
    lampController = object

    def __init__(self):

        # TODO : have this read in from a configuration file
        # initialize Monitron Modules (Mwa Ha Ha)

        # self.tempGetter = TempGetter()     // DS1202B or whatever disabled in favor of combo AM2302

        self.dataStorer = DataStorer()
        self.heatController = HeatController('NormallyON')  # Tell the controller which plug
        self.temperatureAndHumidityGetter = TemperatureAndHumidityGetter('2302', '14') # we're using an AM2302 on pin 6
        self.fanController = FanController(26)              # our fan is a 5V PC fan on pin 26
        self.rgb_led_1 = RGBLEDController(16, 16, 21)       # we're not using the green pins on these.
        self.rgb_led_2 = RGBLEDController(07, 07, 01)       # not using green pins yet maybe
        # the peripherals controlled by the outlet box

        # when the class initializes, set the pins connected to the output box relays
        # accepts key string of corresponding dictionary for outlet number to pin mapping
        # "bcm_pin_dict",  "board_gpio_pin_dict":
        self.outletBoxController = OutletBoxController(0, self.pin_map_key)
        self.outletBoxController.set_pins()
        self.lampController = OutletBoxController(8, self.pin_map_key)          # the lamp is plugged in to outlet 8
        self.humidifierController = OutletBoxController(7, self.pin_map_key)    # the mister is plugged into outlet 7

    def print_status(self):

        # print "%s %s" % (hello, world)
        # print("{} {}".format(hello, world))
        print("|EpochTime: {}\t| Temp : {}\t| Humidity: {}\t".format(TimeGetter.get_epoch_time(), self.currentTemperature, self.currentHumidity))
        print("-----------------------------------------")

    def initialize_peripherals(self):
        self.turn_lights_on()
        self.test_fan()
        self.lampController.turn_outlet_on()

    def turn_lights_on(self):
        self.rgb_led_1.magenta_on()
        print("RGB LED 1 magenta_on")
        self.rgb_led_2.magenta_on()
        print("RGB LED 2 magenta_on")

    def turn_lights_off(self):
        self.rgb_led_1.magenta_off()
        print("RGB LED 1 magenta_off")
        self.rgb_led_2.magenta_off()
        print("RGB LED 2 magenta_off")

    def monitor(self, temperature_min, temperature_max, humidity_min, humidity_max, time_interval):

        while True:

            # get the current temperature and current humidity from the sensor
            self.currentTemperature, self.currentHumidity = self.temperatureAndHumidityGetter.get_temperature_and_humidity('F')

            # store the current temperature and humidity data
            self.dataStorer.store_data(self.currentTemperature, self.currentHumidity)
            print("-----------------------------------------")
            print(TimeGetter.get_epoch_time())

            # TODO : maybe add the fish tank heater in a little pool of water . . .
            # just in case the lamp alone isn't enough to heat the terrarium
            # or the light is too much for the plants over time.
            # i.e. the light has to be on too long to heat the chamber and is cooking the plants.

            # check the temperature conditions, and toggle the heat lamp as necessary

            # if the current temp is lower then the lowest temp minimum we want,
            if float(self.currentTemperature) < float(temperature_min):

                print("Temperature: Low")
                print("{} > {} < {}".format(temperature_min, self.currentTemperature, temperature_max))
                self.lampController.turn_outlet_on()

            # else if the current temp is greater than the max temp we want,
            elif float(self.currentTemperature) > float(temperature_max):

                print("Temperature: High")
                print("{} < {} > {}".format(temperature_min, self.currentTemperature, temperature_max))
                self.lampController.turn_outlet_off()  # turn heat off, if it isn't already off

            else:

                print("Temperature: Sweet Spot")
                print("{} < {} < {}".format(temperature_min, self.currentTemperature, temperature_max))

            # check the humidity conditions and toggle the humidifier as necessary

            # if the current humidity is lower then the lowest humidity minimum we want,
            if float(self.currentHumidity) < float(humidity_min):

                print("Humidity: Low")
                print("{} > {} < {}".format(humidity_min, self.currentHumidity, humidity_max))
                self.humidifierController.turn_outlet_on()

            # else if the current humidity is greater than the max humidity we want,
            elif float(self.currentHumidity) > float(humidity_max):

                print("Humidity: High")
                print("{} < {} > {}".format(humidity_min, self.currentHumidity, humidity_max))
                self.humidifierController.turn_outlet_off()  # turn humidifier off, if it isnt' already off

            else:

                print("Humidity: Sweet Spot")
                print("{} < {} < {}".format(humidity_min, self.currentHumidity, humidity_max))

            # give it a rest. don't spam the sensor too much
            time.sleep(time_interval)

    def monitor_temperature_and_humidity(self, temp_format):
        current_temp, current_humidity = self.temperatureAndHumidityGetter.get_temperature_and_humidity(temp_format)
        print("{0}*{1} {2}".format(current_temp, temp_format, current_humidity))

    def test_rgb_led(self):
        self.rgb_led_1.magenta_on()
        print("RGB LED 1 magenta_on")
        self.rgb_led_2.magenta_on()
        print("RGB LED 2 magenta_on")
        time.sleep(1.5)
        self.rgb_led_1.magenta_off()
        print("RGB LED 1 magenta_off")
        self.rgb_led_2.magenta_off()
        print("RGB LED 2 magenta_off")

    def test_fan(self):

        self.fanController.turn_fan_on()
        print("fan on")
        time.sleep(3)
        self.fanController.turn_fan_off()
        print("fan off")

    def test_lamp(self):
        self.lampController.turn_outlet_on()
        time.sleep(1)
        self.lampController.turn_outlet_off()

    def test_data_storer(self):
        temp_format = 'F'
        current_temp, current_humidity = self.temperatureAndHumidityGetter.get_temperature_and_humidity(temp_format)
        self.dataStorer.store_data(current_temp, current_humidity)
        # print("{0}*{1} {2}".format(current_temp, temp_format, current_humidity))


def main():

    monitron = Monitron()

    monitron.initialize_peripherals()

    # temperature_min, temperature_max, humidity_min, humidity_max, time_interval
    monitron.monitor(70, 80, 70, 80, 3)

    #while True:

        #monitron.test_lamp()
        #monitron.test_fan()
        #monitron.test_rgb_led()
        #monitron.monitor_temperature_and_humidity('F')
        #monitron.test_data_storer()

        #time.sleep(5)

main()
