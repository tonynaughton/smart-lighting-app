#!/usr/bin/python3

# Script used as MQTT publisher to change state of LED

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Parsing MQTT URL for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

# Publish message with 'ON' or 'OFF' message
input = sys.argv[2]
mqttc.publish(base_topic, input)