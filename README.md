<h1>The Smart Lighting App</h1>

Student Name: Tony Naughton

Student ID: 20091454

The Smart Lighting App is designed to control home lighting in an efficient manner. The app provides several methods for switching on/off lighting, through manual and automated processes. For demonstrative purposes, an LED will be used to simulate the lighting.

There are <b>three</b> methods for switching on/off the LED:
1. Interacting with a physical tacticle on/off button which is wired to the Raspberry Pi.
2. Interacting with a virtual on/off button on a webpage.
3. The LED will switch on as when the sun sets, and switch off when the sun has risen.

<h2>Tools, Technologies and Equipment:</h2>

- Raspberry Pi 3 Model B+
- LED
- Tactile push button
- Sunwait
- Flask
- Python
- HTML
- AJAX
- Cron

<h2>Physical ON/OFF button:</h2>

A tactile button is wired up to the Raspberry Pi. When the button is pressed, the state of the LED is changed through button.py.

<h2>Virtual ON/OFF button:</h2>

A Flask server is constantly running on the Raspberry Pi and hosts an interactive webpage which allows a user located in the LAN to switch the LED on/off.

Interacting with button on index.html sends a HTTP Post request using AJAX.

This request calls the ‘led_on’ or ‘led_off’ functions which changes the state of the LED.

<h2>Sunset/Sunrise:</h2>

The level of natural light that in a room will vary all year round as the sun is rising and setting at different times each day.
As a result, the period each day for when artificial light is required will vary.
The time of the sunrise and sunset are found using an existing program called 'Sunwait' (https://github.com/risacher/sunwait).
Cron jobs are used to monitor when the sun has risen or set.

crontab entries:

*/5 * * * * sunwait sun up 51.886661N 8.618732W ; python /home/pi/development/smart-lighting-app/light_on.py

*/5 * * * * sunwait sun down 51.886661N 8.618732W ; python /home/pi/development/smart-lighting-app/light_off.py
