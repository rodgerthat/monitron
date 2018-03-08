# filename TempStorer.py

import time


class TempStorer:

    currentTemp = 0.0

    def __init__(self):

        self.open_create_file

    def open_create_file(self):

        # name file by today's date
        date_today = time.strftime("%Y-%m-%d", time.gmtime())  # get current date

        # filename = date_today + ".dat"

        # f = filename
        # f = open(filename, "w+")

    def create_temp_data(self, incommingTemp):

        self.currentTemp = incommingTemp

    def store_temp(self, incommingTemp):

        # open file,

        f = open('2018-03-04.txt', 'a')	# open logfile for writing
        # right_now = datetime.time(datetime.now())
        right_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        logmsg =  right_now + " " + incommingTemp()
        print(logmsg)
        # print(read_temp())
        # f.write(logmsg)
        # f.close()



