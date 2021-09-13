#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from usbfan import Device, Program, TextMessage
from flask import Flask, render_template, request

# Configure website
app = Flask(__name__)


# Power fan on/off
def change_power(power):
    if power == "on":
        GPIO.output(18, 1)
    else:
        GPIO.output(18, 0)


# Update fan text
def set_text(text):
    GPIO.output(18, 0)
    sleep(5)
    p = Program((TextMessage(text),))
    d = Device()
    d.program(p)
    sleep(5)
    d.program(p)
    sleep(5)
    GPIO.output(18, 1)


# Serve Website
@app.route('/')
def website():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    return render_template('main.html')


# Update text
@app.route('/', methods=['POST'])
def website_set_text():
    text = request.form['text']
    set_text(text)
    return website()

# Power off
@app.route('/off')
def website_power_off():
    change_power("off")


# Power on
@app.route('/on')
def website_power_on():
    change_power("on")


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
