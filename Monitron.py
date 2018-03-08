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

    heatON = False

    def __init__(self):

        # initialize
        self.tempGetter = TempGetter()
        #self.tempStorer = TempStorer()
        self.heatController = HeatController()

    def monitor(self, tempMin, tempMax, timeInterval):

        while True:

            # # get the current temperature in Raw Temp Data, direct from the
            # self.currentTemp = self.tempGetter.get_temp('R')
            # print(self.currentTemp)
            #
            # # get the current temperature in Celcius
            # self.currentTemp = self.tempGetter.get_temp('C')
            # print(self.currentTemp)
            #
            # # get the current temperature in Farenheight
            # self.currentTemp = self.tempGetter.get_temp('F')
            # print(self.currentTemp)

            # test the HeatController
            # if self.heatController.heatON == False:
            #
            #     self.heatController.turn_ON()
            #
            # else:
            #
            #     self.heatController.turn_OFF()

            # get the current temperature in Farenheight
            self.currentTemp = self.tempGetter.get_temp('F')
            print(self.currentTemp)

            # if the current temp is lower then the lowest temp minimum we want,
            if self.currentTemp < tempMin:

                # turn heat on
                self.heatController.turn_ON()
                print(self.heatController.heatON)

            # else if the current temp is greater than the max temp we want,
            elif self.currentTemp > tempMax:

                # turn heat off
                self.heatController.turn_OFF()
                print(self.heatController.heatON)

            # give it a rest. don't spam the sensor too much
            time.sleep(timeInterval)


def main():

    monitron = Monitron()
    #monitron.monitor(80, 90, 5)
    monitron.monitor(80, 83, 1)

main()
