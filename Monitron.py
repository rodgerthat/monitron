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
from Controllers.HeatController import HeatController as HeatController
from Controllers.FanController import FanController as FanController
from Controllers.RGBLEDController import RGBLEDController as RGBLEDController


class Monitron:

    currentTemp = 0.0
    tempGetter = object
    tempStorer = object
    heatController = object
    humidityController = object
    temperatureAndHumidityGetter = object
    fanController = object
    rgb_led_1 = object
    rgb_led_2 = object
    rgb_led_3 = object
    rgb_led_4 = object

    def __init__(self):

        # initialize
        #TODO : have this read in from a configuration file

        #self.tempGetter = TempGetter()     // DS1202B or whatever disabled in favor of combo AM2302
        self.dataStorer = DataStorer()
        self.heatController = HeatController('NormallyON')  # Tell the controller which plug
        self.temperatureAndHumidityGetter = TemperatureAndHumidityGetter('2302', '14')   # we're using an AM2302 on pin 6
        self.fanController = FanController(26)              # our fan is a 5V PC fan on pin 26
        self.rgb_led_1 = RGBLEDController(16,16,21)         # we're not using the green pins on these.

    def print_status(self):

        # print "%s %s" % (hello, world)
        # print("{} {}".format(hello, world))
        print("{} : Temp : {} | heatON : {}".format(TimeGetter.get_epoch_time(), self.currentTemp, self.heatController.heatON))
        print("-----------------------------------------")

    def monitor(self, temp_min, temp_max, time_interval):

        while True:

            # see what's up

            # # get the current temperature in Raw Temp Data, direct from the
            # self.currentTemp = self.tempGetter.get_temp('R', 2)
            # print(self.currentTemp)

            # # get the current temperature in Celsius
            # self.currentTemp = self.tempGetter.get_temp('C', 2)
            # print(self.currentTemp)

            # # get the current temperature in Fahrenheit
            # self.currentTemp = self.tempGetter.get_temp('F', 2)
            # print(self.currentTemp)

            self.currentTemp = self.tempGetter.get_temp('F')
            self.dataStorer.store_data(self.currentTemp)
            print(self.currentTemp)

            # test the HeatController
            # if it's on, turn it off,
            # if it's off, turn it on.
            # if self.heatController.heatON:
            #
            #     self.heatController.turn_OFF()
            #
            # elif not self.heatController.heatON:
            #
            #     self.heatController.turn_ON()

            # else:
            #
            #     self.heatController.turn_ON()

            # give it a rest. don't spam the sensor too much
            time.sleep(time_interval)

    def monitor_heat(self, temp_min, temp_max, time_interval):

        while True:

            # get the current temperature in Fahrenheit
            self.currentTemp = self.tempGetter.get_temp('F')

            self.dataStorer.store_data(self.currentTemp)    # store the current temp

            # if self.currentTemp > temp_min and self.currentTemp < temp_max:
            #
            #     self.heatController.turn_ON()
            #
            # else:
            #
            #     self.heatController.turn_OFF()

            # print("currentTemp : {} | temp_min : {} | temp_max : {}".format(type(self.currentTemp), type(temp_min), type(temp_max)))

            # if the current temp is lower then the lowest temp minimum we want,
            if float(self.currentTemp) < float(temp_min):

                # print("currentTemp : {} < temp_min : {}".format(self.currentTemp, temp_min))
                print("{} : {} > {} | {}".format(TimeGetter.get_epoch_time(), self.currentTemp, temp_min, self.currentTemp < temp_min))
                self.heatController.turn_ON()   # turn heat on

            # else if the current temp is greater than the max temp we want,
            elif float(self.currentTemp) > float(temp_max):

                # print("currentTemp : {} > temp_max : {}".format(self.currentTemp, temp_max))
                print("{} : {} > {} | {}".format(TimeGetter.get_epoch_time(), self.currentTemp, temp_max, self.currentTemp > temp_max))
                self.heatController.turn_OFF()  # turn heat off, if it isnt' already off

            # else:

                # print("Neither condition has been met")

            # TODO : Add a default case else here
            # checkitty check yo sef b4 u wreck yo sef
            self.print_status()

            # give it a rest. don't spam the sensor too much
            time.sleep(time_interval)

    def test_rgb_led(self):
        self.rgb_led_1.magenta_on()
        time.sleep(3)
        self.rgb_led_1.magenta_off()

    def monitor_temperature_and_humidity(self):
        temp_format = 'F'
        current_humidity, current_temp = self.temperatureAndHumidityGetter.get_temperature_and_humidity(temp_format)
        print("{0}*{1} {2}".format(current_temp, temp_format, current_humidity))

    def test_fan(self):

        self.fanController.turn_fan_on()
        print("fan on")
        time.sleep(3)
        self.fanController.turn_fan_off()
        print("fan off")


def main():

    monitron = Monitron()
    # monitron.monitor(80, 90, 60)
    # monitron.monitor_heat(80, 90, 60)

    # monitron.test_fan()

    while True:
        monitron.test_rgb_led()
        monitron.monitor_temperature_and_humidity()


main()
