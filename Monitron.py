# filename: monitron.py
# author: rodgerthat
# description:
# monitors shed 1

import time

import Getters.TempGetter
import Setters.TempStorer
import Controllers.HeatController


class Monitron:

    currentTemp = 0.0
    tempGetter = object
    tempStorer = object

    heatON = False

    def __init__(self):

        # initialize
        self.tempGetter = Getters.TempGetter.TempGetter()
        self.tempStorer = Setters.TempStorer.TempStorer()
        self.heatController = Controllers.HeatController.HeatController()

    def monitor(self, tempMin, tempMax, timeInterval):

        while True:

            # get the current temperature in Raw Temp Data
            #self.currentTemp = self.tempGetter.get_temp('R')
            #print(self.currentTemp)

            # get the current temperature in Celcius
            #self.currentTemp = self.tempGetter.get_temp('C')
            #print(self.currentTemp)

            # get the current temperature in Farenheight
            #self.currentTemp = self.tempGetter.get_temp('F')
            #print(self.currentTemp)

            # test the HeatController
            if self.heatController.heatON == False:
                self.heatController.turn_ON()
            else:
                self.heatController.turn_OFF()

            # self.currentTemp = self.tempGetter.get_temp('C')
            #
            # if self.currentTemp < tempMin:
            #
            #     # turn heat on
            #     self.heatON = True
            #     self.heatController.turnON()
            #
            # elif self.currentTemp > tempMax:
            #
            #     # turn heat off
            #     self.heatON = False
            #     self.heatController.turnOFF()

            # give it a rest. don't spam the sensor too much
            time.sleep(timeInterval)


def main():

    monitron = Monitron()
    monitron.monitor(70, 80, 5)


main()
