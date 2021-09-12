#!/usr/bin/python

import argparse
import RPi.GPIO as GPIO
from time import sleep
from usbfan import Device, Program, TextMessage


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


# Configure relay
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--text", "-t", help="set text to be displayed")
parser.add_argument("--power", "-p", help="enable/disable fan")
args = parser.parse_args()

if args.power:
    if args.power == "on" or args.power == "off":
        change_power(args.power)
        exit()

if args.text:
    text = str(args.text)
else:
    text = "DIYODE"

set_text(text)