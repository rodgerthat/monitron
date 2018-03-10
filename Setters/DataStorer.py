# filename TempStorer.py

import time
import datetime
import os


# TODO: data_to_store should be an array or some other structure that can pass thru multiple data
class DataStorer:

    currentTemp = 0.0
    currentFile = object
    currentFileName = 'currentFileName.csv'
    currentFilePath = os.getcwd() + '/DataLogs/currentFile.csv'
    currentEpochTime = int(time.time())
    dataLogsDirectoryName = 'DataLogs'

    def __init__(self):

        self.create_file()

    def create_file(self):

        current_date_time = datetime.datetime.now()
        self.currentFileName = 'DataLog-%s-%s-%s.csv' % (current_date_time.year, current_date_time.month, current_date_time.day)
        self.currentFilePath = "{}/{}/{}".format(os.getcwd(), self.dataLogsDirectoryName, self.currentFileName)

        # check if a file has already been created today,
        # if not, create it, if so, don't
        if not os.path.exists(self.currentFilePath):

            print(self.currentFilePath)
            self.currentFile = open(self.currentFilePath, "w+")
            self.currentFile.write("td, t1")
            self.currentFile.close()

    def create_storable_data(self, data_to_store):

        # create a csv string with epoch time and temp data
        self.currentTemp = data_to_store
        self.currentEpochTime = int(time.time())

        storable_data = "{}, {}\n".format(self.currentEpochTime, self.currentTemp)

        return storable_data

    def store_data(self, data_to_store):

        storable_data = self.create_storable_data(data_to_store)

        # open file, to append with data
        self.currentFile = open(self.currentFilePath, "a")
        self.currentFile.write(storable_data)
        self.currentFile.close()




