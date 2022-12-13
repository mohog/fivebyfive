import config
import network
from machine import Pin
from neopixel import NeoPixel
# setup the status LED
status_led = Pin(10, Pin.OUT)


print("Connecting to wifi...")

# Activate the station interface
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Connect to your wifi network
sta_if.connect(config.ssid, config.password)
# Wait until the wireless is connected
while not sta_if.isconnected():
    pass
status_led.on()  # status LED shows connected
# Print out the network configuration received from DHCP
print('network config:', sta_if.ifconfig())

