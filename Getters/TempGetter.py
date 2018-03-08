# filename: GetTemp.py
# author: rodgerthat
# description:

import os
import glob


# TODO: add additional class constructor param to accept which device (i.e. multiple temp sensors)
class TempGetter:

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    raw_temp = 0
    temp_string = '0'

    # main method of functionality for class
    # get a temperature from a temp sensor and return it in requested format
    def get_temp(self, temp_format):

        self.raw_temp = self.read_temp_raw()

        self.temp_string = self.read_temp()

        # in Celsius
        if temp_format == 'C':
            return self.convert_to_celcius()

        # in Fahrenheit
        elif temp_format == 'F':
            return self.convert_to_farenheight()

        # Raw Temp Sensor Data
        elif temp_format == 'R':
            return self.raw_temp

        else:
            return 'No Format Specified'

    # converts the base raw temp integer to celsius by dividing by a float of 1000.0
    # this just adds a decimal to it
    def convert_to_celcius(self):

        return float(self.temp_string) / 1000.0

    # converts temp data from celsius to fahrenheit
    def convert_to_farenheight(self):

        return (self.convert_to_celcius()) * 9.0 / 5.0 + 32.0

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

