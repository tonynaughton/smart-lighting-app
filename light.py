#Script for controlling the LED based on the time of day

import RPi.GPIO as GPIO
import time
from sys import argv

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

timeOfDay=argv[1]

if timeOfDay=="NIGHT":
	GPIO.output(18,GPIO.HIGH);
	print ("Light has been switched on")
elif timeOfDay=="DAY":
	GPIO.output(18,GPIO.LOW);
	print ("Light has been switched off")
