# filename TempStorer.py

import time
import datetime
import os
from Getters.TimeGetter import TimeGetter as TimeGetter


# TODO: data_to_store should be an array or some other structure that can pass thru multiple data
class DataStorer:

    currentTemp = 0.0
    currentFile = object
    currentFileName = 'currentFileName.csv'
    # this returns the path to the location where python was executed.
    currentFilePath = os.getcwd() + '/DataLogs/currentFile.csv'
    # currentFilePath = os.path.dirname(os.path.realpath(__file__))
    currentEpochTime = TimeGetter.get_epoch_time()
    dataLogsDirectoryName = 'DataLogs'
    dataLogFilePath = 'home/pi/MTMT/Monitron'   # hopefully

    def __init__(self):

        self.create_file()

    def create_file(self):

        current_date_time = datetime.datetime.now()
        # TODO : clean up the pathfinding, try not to use os.getcwd() down here, but rather up in properties.
        self.currentFileName = 'DataLog-%s-%s-%s.csv' % (current_date_time.year, current_date_time.month, current_date_time.day)
        self.currentFilePath = "{}/{}/{}".format(os.getcwd(), self.dataLogsDirectoryName, self.currentFileName)

        # check if a file has already been created today,
        # if not, create it, if so, don't
        if not os.path.exists(self.currentFilePath):

            print(self.currentFilePath)
            self.currentFile = open(self.currentFilePath, "w+")
            self.currentFile.write("epoch_time, humidity, temperature\n")       # I always forget the \n
            self.currentFile.close()

    def format_data_string(self, current_temp, current_humidity):

        # create a csv string with epoch time and temp and humidity data
        self.currentEpochTime = int(time.time())

        data_string = "{}, {}, {}\n".format(self.currentEpochTime, current_temp, current_humidity)

        # print(data_string)

        return data_string

    def store_data(self, current_temp, current_humidity):

        data_string = self.format_data_string(current_temp, current_humidity)

        # open file, to append with data string
        self.currentFile = open(self.currentFilePath, "a")
        self.currentFile.write(data_string)
        self.currentFile.close()




