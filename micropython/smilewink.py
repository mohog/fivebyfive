# inspired from https://twitter.com/GeekMomProjects/status/1483695065629224960

# this is a random color, random display and sleep length smiley face that winks
# should not require any additional Python modules outside of core MicroPython

from machine import Pin
from neopixel import NeoPixel
import random
import time

# setup the NeoPixels

neopin = Pin(8, Pin.OUT)  # NeoPixel control on Pin 8
pixels = 25  # we have 25 pixels, set as a constant here for loops

np = NeoPixel(neopin, pixels)

# setup the button and the status LED
button = Pin(9, Pin.IN)
status_led = Pin(10, Pin.OUT)

def rand_rgb():
    # Return a randomised RGB tuple, max values of 50 to limit brightness
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    return r, g, b

def clear_all():
    # Reset all Neopixels to black / off
    # TODO: could have this use a custom colour
    np.fill((0, 0, 0))
    np.write()

def smile():
    # Light the pixels into a smiley face
    lights = [1, 3, 12, 15, 19, 21, 22, 23]
    for x in lights:
        np[x] = rgb
        np[20] = 0,0,0
        np[24] = 0,0,0
    np.write()

def mmmm():
    # Light the pixels into a mmmm face
    lights = [1, 3, 12, 20, 24, 21, 22, 23]
    for x in lights:
        np[x] = rgb
        np[15] = 0,0,0
        np[19] = 0,0,0
    np.write()
    
def wink():
    # Light the pixels into wink face
    lights = [3]
    for x in lights:
        np[x] = 0,0,0
    np.write()

# run the functions
while True:
 r = random.randint(0,25)
 g = random.randint(0,25)
 b = random.randint(0,25)
 rgb=[r,g,b]
 mmmm()
 time.sleep(1)
 smile()
 time.sleep(0.3)
 wink()
 time.sleep(0.3)
 smile()
 ranshow = random.randint(1,5)
 time.sleep(ranshow)
 clear_all()
 ransleep = random.randint(1,2)
 time.sleep(ransleep)

 

