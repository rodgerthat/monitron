# filename: monitron.py
# author: rodgerthat
# description:
# monitors shed 1

import os
import sys
import time

from Getters.TempGetter import TempGetter
#from Setters.TempStorer import TempStorer
from Controllers.HeatController import HeatController


class Monitron:

    currentTemp = 0.0
    tempGetter = object
    tempStorer = object
    heatController = object

    def __init__(self):

        # initialize
        self.tempGetter = TempGetter()
        # self.tempStorer = TempStorer()
        self.heatController = HeatController('NormallyON')  # Tell the controller which plug

    def print_status(self):

        # print "%s %s" % (hello, world)
        # print("{} {}".format(hello, world))
        print("Temp : {} | heatON : {}".format(self.currentTemp, self.heatController.heatON))
        print("-----------------------------------------")

    def monitor(self, temp_min, temp_max, time_interval):

        while True:

            # see what's up

            # # get the current temperature in Raw Temp Data, direct from the
            # self.currentTemp = self.tempGetter.get_temp('R')
            # print(self.currentTemp)
            #
            # # get the current temperature in Celsius
            # self.currentTemp = self.tempGetter.get_temp('C')
            # print(self.currentTemp)
            #
            # # get the current temperature in Fahrenheit
            # self.currentTemp = self.tempGetter.get_temp('F')
            # print(self.currentTemp)

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

            # get the current temperature in Fahrenheit
            self.currentTemp = self.tempGetter.get_temp('F')

            # if the current temp is lower then the lowest temp minimum we want,
            if self.currentTemp < temp_min:

                print("currentTemp : {} < temp_min : {}".format(self.currentTemp, temp_min))

                # turn heat on
                self.heatController.turn_ON()

            # else if the current temp is greater than the max temp we want,
            elif self.currentTemp > temp_max:

                print("currentTemp : {} < temp_max : {}".format(self.currentTemp, temp_min))

                # turn heat off, if it isnt' already off
                self.heatController.turn_OFF()

            # checkitty check yo sef b4 u wreck yo sef
            self.print_status()

            # give it a rest. don't spam the sensor too much
            time.sleep(time_interval)


def main():

    monitron = Monitron()
    # monitron.monitor(80, 90, 3)   # just for heat controller test
    monitron.monitor(80, 90, 1)


main()
