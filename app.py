from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_on', methods=['POST'])
def led_on():
	GPIO.output(18,GPIO.HIGH)
	print("Light has been switched on")
@app.route('/led_off', methods=['POST'])
def led_off():
        GPIO.output(18,GPIO.LOW)
	print("Light has been switched off")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
