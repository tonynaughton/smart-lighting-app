#!/usr/bin/python3

import light
from flask import Flask, render_template
from gpiozero import Button, LED
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route which calls the light_switch function for changing state of LED
@app.route('/led_toggle', methods=['POST'])
def led_toggle():
    light.light_switch()
    print("Light has been switched off")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
