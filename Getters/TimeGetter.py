# filename: TimeGetter.py
# author: rodgerthat
# description: A Class to get temperature data from DS18B-something temp sensors.
# note: everything in linux is a file.

import time

# TODO: add additional class constructor param to accept which device (i.e. multiple temp sensors)
class TimeGetter:

    # constructor
    def __init__(self):
        pass

    @staticmethod
    def get_epoch_time():

        return int(time.time())
