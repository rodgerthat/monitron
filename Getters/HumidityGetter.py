# filename: HumidityGetter.py
# author: rodgerthat
# description: A Class to get humidity data from AOSONG AM2320 combination humidity / temp sensors.
# url: https://akizukidenshi.com/download/ds/aosong/AM2320.pdf

import os
import glob
import sys
import Adafruit_DHT
from decimal import Decimal


# TODO: add additional class constructor param to accept which device (i.e. multiple temp sensors)
class HumidityGetter:

    sensor_types = {
        '11': Adafruit_DHT.DHT11,
        '22': Adafruit_DHT.DHT22,
        '2320': Adafruit_DHT.AM2320
    }

    sensor = ''
    pin = ''

    # constructor
    # pass the GPIO pin and sensor type into the class properties
    def __init__(self, sensor_type, pin):
        self.sensor = self.sensor_types[sensor_type]
        self.pin = pin

    # get humidity reading
    def get_humidity(self):
        humidity = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity

    def get_temp(self, temp_format):
        temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temp_format == 'C':
            return temperature
        if temp_format == 'F':
            return temperature * 9/5.0 + 32

    def get_humidity_and_temp(self, temp_format):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        humidity, temperature = self.format_sensor_data(humidity, temperature)
        if temp_format == 'C':
            return humidity, temperature
        if temp_format == 'F':
            return humidity, temperature * 9/5.0 + 32

    @staticmethod
    def format_sensor_data(humidity, temperature):
        if humidity is not None and temperature is not None:
            humidity = '1:0.1f'.format(humidity)
            temperature = '0:0.1f'.format(temperature)
            return humidity, temperature
        else:
            return 'Failed to get reading, try again'
