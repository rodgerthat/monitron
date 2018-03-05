# filename: GetTemp.py
# author: rodgerthat
# description:

import os
import glob
import time

class TempGetter:

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    rawTemp = 0

    # main method of functionality for class
    # get a temperature from a temp sensor and return it in requested format
    # TODO: add additional param for temp formatting, raw, C, F, K, Whatevs
    def getTemp(self):

        self.rawTemp = self.read_temp_raw()

        return self.rawTemp

    # open the device and read the temp from the file (everything in linux is a file)
    # read it, then close the file,
    # returns the file data
    def read_temp_raw(self):

        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    # reads the lines and splits after the key values before the data
    # converts to normal celcius value and returns that and converts to degrees F
    def read_temp(self):

        lines = self.read_temp_raw()

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.05)
            lines = self.read_temp_raw()

        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            #return int(temp_string)
            #return temp_c
            temp_string = str(temp_f)
            return temp_string

