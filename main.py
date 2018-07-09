from flask import Flask
import RPi.GPIO as GPIO
import threading
import subprocess 

import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
    
app = Flask(__name__)
@app.route('/forward')
def forward():
    GPIO.output(21, 1)
    GPIO.output(20, 0)
    GPIO.output(26, 1)
    GPIO.output(19, 0)
    time.sleep(5)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    
    return "Hello World!"

@app.route('/backward')
def backward():
    GPIO.output(21, 0)
    GPIO.output(20, 1)
    GPIO.output(26, 0)
    GPIO.output(19, 1)
    time.sleep(5)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    
    return "Hello World! off"

@app.route('/right')
def left():
    GPIO.output(21, 1)
    GPIO.output(20, 0)
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    time.sleep(2.5)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    return "Hello World!"

@app.route('/test')
def test():    
    subprocess.call("python label.py", shell=True)
    return "Hello World!"


@app.route('/left')
def right():
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(26, 1)
    GPIO.output(19, 0)
    time.sleep(2.5)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    
    return "Hello World!"