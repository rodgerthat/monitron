# filename: monitron.py
# author: rodgerthat
# description:
# monitors shed 1

import os
import sys
import time

from Getters.TempGetter import TempGetter
#from Setters.TempStorer import TempStorer.TempStorer
from Controllers.HeatController import HeatController

#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


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

            # # get the current temperature in Raw Temp Data
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
            if self.heatController.heatON == False:
                self.heatController.turn_ON()
            else:
                self.heatController.turn_OFF()

            # self.currentTemp = self.tempGetter.get_temp('C')

            # if it's currently lower then as low as we want it.
            if self.currentTemp < tempMin:

                # turn heat on
                self.heatController.turn_ON()

            elif self.currentTemp > tempMax:

                # turn heat off
                self.heatController.turn_OFF()

            # get the current temperature in Celcius
            self.currentTemp = self.tempGetter.get_temp('C')
            print(self.currentTemp)
            self.currentTemp = self.tempGetter.get_temp('F')
            print(self.currentTemp)

            # give it a rest. don't spam the sensor too much
            time.sleep(timeInterval)


def main():

    monitron = Monitron()
    monitron.monitor(70, 80, 5)


main()
