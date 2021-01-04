#!/usr/bin/python3

# Script which is called by Cron for switching LED off

from gpiozero import LED
from time import sleep

led = LED(18)

led.off()
print ("The light is switched OFF")