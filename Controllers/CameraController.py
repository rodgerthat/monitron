"""
 " ;FileName: CameraController
 " ;Author: goat 
 " ;Created: 7/4/18
 " ;Description:
 " ;URL
 """

from picamera import PiCamera
import time


class CameraController:

    camera = object

    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180

    def take_picture(self):
        self.camera.start_preview()
        time.sleep(1)
        self.camera.capture('/home/pi/MTMT/Monitron/static/images/recent.jpg')
        self.camera.stop_preview()
