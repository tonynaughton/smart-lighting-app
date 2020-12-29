from gpiozero import LED
from time import sleep

led = LED(18)

def light_on():
	led.on()
	print ("Light has been switched on")

def light_off():
	led.off()
	print ("Light has been switched off")

def light_switch():
	led.toggle()
	

