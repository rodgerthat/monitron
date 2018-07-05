"""
 " ;FileName: CameraStream
 " ;Author: goat 
 " ;Created: 7/4/18
 " ;Description:
 " ;URL
 """

from bottle import Bottle, route, response, run
import io
import picamera
import numpy as np
import time
import traceback, sys

BOUNDARY = '--jpgboundary'


@route('/index.html')
def index():
    return '''
        <html>
            <head>
                <title>CSCI_4600 : Remote Venus FlyTrap Terrarium Control</title>
            </head>
            <body>
                <h1>CSCI 4600 : Venus FlyTrap Terrarium Remote Control</h1>
                <img src="/stream.mjpg" />
                <h2>Hi Jenny!</h2>
            </body>
        </html>
        '''


@route('/stream.mjpg')
def mjpeg():
    response.content_type = 'multipart/x-mixed-replace;boundary=%s' % BOUNDARY
    stream = io.BytesIO()
    yield BOUNDARY + '\r\n'
    with picamera.PiCamera() as camera:
        camera.rotation = 180
        camera.resolution = (640, 480)
        for picture in camera.capture_continuous(stream, 'jpeg'):
            yield BOUNDARY + '\r\n'
            yield 'Content-Type: image/jpeg\r\nContent-Length: %s\r\n\r\n' % len(stream.getvalue())
            yield stream.getvalue()
            stream.seek(0)
            stream.truncate()
            time.sleep(.1)


run(reloader=True, host='192.168.1.146', port=8080, debug=True)
#run(reloader=True, host='192.168.1.146', port=8080, server='gevent', debug=True)
#run(reloader=True, host='192.168.1.146', port=8080, server='gunicorn', debug=True)
