# filename: monitron.py
# author: rodgerthat
# description:
# monitors shed 1

import time

from TempGetter import TempGetter
from TempStorer import TempStorer


class Monitron:

    currentTemp = 0.0
    tempGetter = object
    tempStorer = object

    def __init__(self):

        # initialize
        self.tempGetter = TempGetter()
        self.tempStorer = TempStorer()

    def monitor(self, tempMin, tempMax):

        while True:

            self.currentTemp = self.tempGetter.get_temp('R')
            print(self.currentTemp)

            self.currentTemp = self.tempGetter.get_temp('C')
            print(self.currentTemp)

            self.currentTemp = self.tempGetter.get_temp('F')
            print(self.currentTemp)

            time.sleep(5)


def main():

    monitron = Monitron()
    monitron.monitor(70, 80)


main()
