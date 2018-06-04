# filename: TempGetter.py
# author: rodgerthat
# description: A Class to get temperature data from DS18B-something temp sensors.
# note: everything in linux is a file.

import os
import glob
from decimal import Decimal


# TODO: add additional class constructor param to accept which device (i.e. multiple temp sensors)
class TempGetter:

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    rawTemp = 0
    tempString = '0'
    numDecimalPlaces = 2

    # constructor
    def __init__(self):
        pass

    # main method of functionality for class
    # get a temperature from a temp sensor and return it in requested format
    def get_temp(self, temp_format):

        self.rawTemp = self.read_temp_raw()

        self.tempString = self.read_temp()

        # in Celsius
        if temp_format == 'C':
            return self.convert_to_celsius()

        # in Fahrenheit
        elif temp_format == 'F':
            return self.convert_to_fahrenheit()

        # Raw Temp Sensor Data
        elif temp_format == 'R':
            return self.rawTemp

        else:
            return 'No Format Specified'

    # def round_it(self, num_to_be_rounded):
    #
    #     # First we take a float and convert it to a decimal
    #     decimal_temp = Decimal(num_to_be_rounded)
    #
    #     # Then we round it to 2 places
    #     return round(decimal_temp, self.numDecimalPlaces)

    # converts the base raw temp integer to celsius by dividing by a float of 1000.0
    # this just adds a decimal to it
    def convert_to_celsius(self):

        # TODO : find a way to control the number of decimal places dynamically.
        temp_celsius = float(self.tempString) / 1000.0
        return "{0:.2f}".format(temp_celsius);
        # TODO : use this for rounding, then return float value
        # return round("{0:.2f}".format(temp_celsius), self.numDecimalPlaces)

        # return self.round_it(temp_celsius)
        # return float(self.tempString) / 1000.0

    # converts temp data from celsius to fahrenheit
    def convert_to_fahrenheit(self):

        temp_fahrenheit = (float(self.tempString) / 1000.0) * 9.00 / 5.00 + 32.00
        return "{0:.2f}".format(temp_fahrenheit);

        # return self.round_it(temp_fahrenheit)
        # return (self.convert_to_celsius()) * 9.0 / 5.0 + 32.0

    # returns the raw data from the temp sensor
    def read_temp_raw(self):

        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    # reads the lines and splits after the key values before the data
    def read_temp(self):

        lines = self.read_temp_raw()

        while lines[0].strip()[-3:] != 'YES':
            # time.sleep(0.05)
            lines = self.read_temp_raw()

        equals_pos = lines[1].find('t=')

        if equals_pos != -1:

            return lines[1][equals_pos+2:]

