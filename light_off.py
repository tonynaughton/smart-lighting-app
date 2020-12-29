from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.off()
    print ("Light has been switched off")
    sleep(0.5)