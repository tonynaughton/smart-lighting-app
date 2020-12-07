<h1>The Smart Lighting App</h1>

Student Name: Tony Naughton

Student ID: 20091454

The Smart Lighting App incorporates several methods if switching on a light, through natural and interactive processes. For demonstrative purposes, an LED will simulate the light.

There are <b>three</b> possible ways the LED is switched on/off:
1. The LED will switch on as the sun is setting, and switch off as the sun rises.
2. Interacting with a physical tacticle on/off switch which is wired to the Raspberry Pi.
3. Interacting with a virtual on/off switch on the project's website.

<h2>Sunset/Sunrise control:</h2>

The level of natural light that in a room will vary all year round as the sun is rising and setting at different times each day.
As a result, the period each day for when artificial light is required will vary.
The time of the sunrise and sunset are found using an existing program called 'Sunwait'.
The cron daemon is used to monitor when the sun has risen or set.

crontab entries:

5 * * * * sunwait sun up 51.886661N 8.618732W ; python /home/pi/development/smart-lighting-app/light.py DAY

5 * * * * sunwait sun down 51.886661N 8.618732W ; python /home/pi/development/smart-lighting-app/light.py NIGHT

<h2>Flask Server</h2>

A Flask server runs on the Raspberry Pi and hosts an interactive web page which allows a user located in the LAN to switch the LED on or off.

Interacting with button on index.html sends a HTTP Post request using AJAX.

This request calls the ‘led_on’ or ‘led_off’ function which changes the state of the LED.

Tools, Technologies and Equipment:

- Raspberry Pi 3 Model B+
- LED (simulates the light)
- Tactile push button
- Sunwait
- Flask framework
- Python
- HTML
- AJAX
- Thingspeak
- cron
