"""
 " ;FileName: HelloWorld.py
 " ;Author: goat 
 " ;Created: 7/4/18
 " ;Description:
 " ;URL: https://bottlepy.org/docs/0.12
 """

from bottle import Bottle, route, run

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

run(app, host='192.168.1.146', port=8080, debug=True)


