import light
from flask import Flask, render_template
from gpiozero import Button, LED
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_on', methods=['POST'])
def led_on():
	light.light_on()
	print("Light has been switched on")

@app.route('/led_off', methods=['POST'])
def led_off():
    light.light_off()
    print("Light has been switched off")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
