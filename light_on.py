from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    print ("Light has been switched on")
    sleep(0.5)