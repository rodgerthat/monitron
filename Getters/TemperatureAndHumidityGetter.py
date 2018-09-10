# filename: HumidityGetter.py
# author: rodgerthat
# description: A Class to get humidity data from AOSONG AM2302 combination humidity / temp sensors.
# url: https://akizukidenshi.com/download/ds/aosong/AM2302.pdf

import os
import glob
import sys
import Adafruit_DHT


class TemperatureAndHumidityGetter:

    sensor_types = {
        '11': Adafruit_DHT.DHT11,
        '22': Adafruit_DHT.DHT22,
        '2302': Adafruit_DHT.AM2302
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
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity

    def get_temp(self, temp_format):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temp_format == 'C':
            return temperature
        if temp_format == 'F':
            return temperature * 9/5.0 + 32

    def get_temperature_and_humidity(self, temp_format):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        print(temperature, humidity)
        temperature, humidity = self.format_sensor_data(temperature, humidity)
        if temp_format == 'C':
            return temperature, humidity
        if temp_format == 'F':
            temperature = float(temperature) * 9/5.0 + 32
            return temperature, humidity

    @staticmethod
    def format_sensor_data(temperature, humidity):
        if temperature is not None and humidity is not None:
            formatted_humidity = "{0:0.1f}".format(humidity)
            formatted_temperature = "{0:0.1f}".format(temperature)
            return formatted_temperature, formatted_humidity
        else:
            return 'Failed to get reading, try again'
