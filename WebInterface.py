"""
 " ;FileName: WebInterface
 " ;Author: goat 
 " ;Created: 7/4/18
 " ;Description: I'm going to acknowledge at present this file is attrocious.
 "      It's my first attempt at a larger scale python app controlled via a web interface
 " ;URL: https://electronut.in/talking-to-a-raspberry-pi-from-your-phone-using-bottle-python/
 """

from bottle import route, request, run, response, get, static_file, template

import io
import picamera
import time

from Monitron import Monitron

BOUNDARY = '--jpgboundary'

monitron = Monitron()

'''
# in the tutorial this is where they set up the pin configuration
# we're not doing that since it's handled elsewhere in the classes
# that directly interface with the pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)
'''


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pi/MTMT/Monitron/static/')


@route('/index')
def index():

    currentTemperature, currentHumidity = monitron.temperatureAndHumidityGetter.get_temperature_and_humidity('F')

    # TODO : pass in a dict
    return template('''
        <html>
            <head>
                <title>CSCI_4600 : Remote Venus FlyTrap Terrarium Control</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css">
                <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
                <script src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
                <script>
                    $(document).ready(function() {
                        $("#checkbox_lamp").change(function() {
                            var isChecked = $("checkbox_lamp").is(":checked") ? 1:0;
                            $.ajax({
                                url: "/action",
                                type: "POST",
                                data: {control_id:"checkbox_lamp", strState:isChecked}
                            });
                        });
                        $("#checkbox_rgb_led").change(function() {
                            var isChecked = $("checkbox_rgb_led").is(":checked") ? 1:0;
                            $.ajax({
                                url: "/action",
                                type: "POST",
                                data: {control_id:"checkbox_rgb_led", strState:isChecked}
                            });
                        });
                        $("#checkbox_fan").change(function() {
                            var isChecked = $("checkbox_fan").is(":checked") ? 1:0;
                            $.ajax({
                                url: "/action",
                                type: "POST",
                                data: {control_id:"checkbox_fan", strState:isChecked}
                            });
                        });
                        $("#checkbox_humidifier").change(function() {
                            var isChecked = $("checkbox_humidifier").is(":checked") ? 1:0;
                            $.ajax({
                                url: "/action",
                                type: "POST",
                                data: {control_id:"checkbox_humidifier", strState:isChecked}
                            });
                        });
                        $("#button_take_pic").click(function() {
                            console.log("clicka clicka");
                            $.ajax({
                                url: "/action",
                                type: "POST",
                                data: {control_id:"button_take_pic"},
                                success: image_refresh
                            });
                        });
                    });
                    console.log("<3 Hi Jenny!");
                    function image_refresh() {
                        $("#recent_pic").attr("src", $("#recent_pic").attr("src") + "?" + Math.random() );
                    }
                </script>
                <style>
                    img { width: 100%; }
                
                </style>
            </head>
            <body>
                <div data-role="page">
                    <div data-role="main" class="ui-content">
                    
                        <h1>CSCI 4600 : Venus FlyTrap Terrarium Remote Control</h1>
                        
                        <div class="ui-grid-a">
                        
                            <h3>Termperature : {{temp}} *F</h3><h3>Humidity : {{humid}}</h3>
                        
                        </div><!-- /.ui-grid-a -->
                        
                        <div class="ui-grid-a">
                            <div class="ui-block-a">
                            
                                <form>
                                    <label for="switch">Lamp Control</label>
                                    <input type="checkbox" data-role="flipswitch" name="switch" id="checkbox_lamp">
                                    <label for="switch">RGB LED Control</label>
                                    <input type="checkbox" data-role="flipswitch" name="switch" id="checkbox_rgb_led">
                                    <label for="switch">Fan Control</label>
                                    <input type="checkbox" data-role="flipswitch" name="switch" id="checkbox_fan">
                                    <label for="switch">Humidifier Control</label>
                                    <input type="checkbox" data-role="flipswitch" name="switch" id="checkbox_humidifier">
                                </form>
                                
                            </div><!-- /.ui-block-a -->
                            
                            <div class="ui-block-b">
                            
                                <!-- <img src="/stream.mjpg" /> -->
                                <button data-role="button" id="button_take_pic">Take a Picture!</button>
                                <img id="recent_pic" src="static/images/recent.jpg" alt="most recent cam pic" />
                                <h2>Hi Jenny! <3</h2>
                                
                            </div><!-- /.ui-block-b -->
                            
                        </div><!-- /.ui-grid-a -->
                        
                        <form>
                            <label for="slider_temp_min">Set Temperature Minimum</label>
                            <input type="range" name="slider-fill" id="slider_temp_min" value="60" min="40" max="65" data-highlight="true">
                            <label for="slider_temp_max">Set Temperature Maximum:</label>
                            <input type="range" name="slider-fill" id="slider_temp_max" value="80" min="65" max="95" data-highlight="true">
                            
                            <label for="slider_humid_min">Set Humidity Minimum</label>
                            <input type="range" name="slider-fill" id="slider_humid_min" value="55" min="50" max="60" data-highlight="true">
                            <label for="slider_humid_max">Set Humidity Maximum:</label>
                            <input type="range" name="slider-fill" id="slider_humid_max" value="69" min="60" max="70" data-highlight="true">
                        </form>
                        
                    </div><!-- /.ui-content -->
                <div>
            
            </body>
        </html>
    ''', temp=currentTemperature, humid=currentHumidity)


@route('/action', method='POST')
def action():

    control_id = request.forms.get('control_id')

    print(control_id)

    if control_id == 'checkbox_lamp':

        if not monitron.lampController.is_on:
            monitron.lampController.turn_outlet_on()
        else:
            monitron.lampController.turn_outlet_off()

    if control_id == 'checkbox_rgb_led':

        if not monitron.rgb_led_1.is_on:
            monitron.rgb_led_1.magenta_on()
        else:
            monitron.rgb_led_1.magenta_off()

        if not monitron.rgb_led_2.is_on:
            monitron.rgb_led_2.magenta_on()
        else:
            monitron.rgb_led_2.magenta_off()

    if control_id == 'checkbox_fan':
        if not monitron.fanController.is_on:
            monitron.fanController.turn_on()
        else:
            monitron.fanController.turn_off()

    if control_id == 'checkbox_humidifier':
        if not monitron.humidifierController.is_on:
            monitron.humidifierController.turn_outlet_on()
        else:
            monitron.humidifierController.turn_outlet_off()

    if control_id == 'button_take_pic':

        monitron.cameraController.take_picture()
        print("took pic")


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
            time.sleep(1)


def run_server():
    run(host='192.168.1.146', port=8080, debug=True)


def main():
    run_server()


main()
