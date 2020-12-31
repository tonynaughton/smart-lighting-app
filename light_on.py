from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    print ("The light is switched ON")
    sleep(300.0)