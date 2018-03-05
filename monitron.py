# filename: monitron.py
# author: rodgerthat
# description:
# monitors shed 1


import time
from threading import Timer

from datetime import datetime
from time import gmtime, strftime

import TempGetter
import TempStorer


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

            self.currentTemp = self.tempGetter.getTemp()

            print(self.currentTemp)


def main():

    monitron = Monitron()
    monitron.moitor(70, 80)


main()
