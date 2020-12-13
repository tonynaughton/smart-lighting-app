# Script for switching LED on/off uisng button

from gpiozero import LED, Button
from time import sleep

led = LED(18)
button = Button(22)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)