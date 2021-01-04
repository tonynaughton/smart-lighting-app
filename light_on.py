#!/usr/bin/python3

# Script which is called by Cron for switching LED on

from gpiozero import LED
from time import sleep

led = LED(18)

led.on()
print ("The light is switched ON")