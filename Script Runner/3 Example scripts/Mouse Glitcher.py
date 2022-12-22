# youtube.com/technotebook
import time
import os
import random
import usb_hid
from adafruit_hid.mouse import Mouse

time.sleep(1.5)

def click():
    mouse.press(Mouse.LEFT_BUTTON)
    #time.sleep(0.01)
    mouse.release(Mouse.LEFT_BUTTON)

mouse = Mouse(usb_hid.devices)
x = 100
while x != 0:
    mouse.move(random.randint(-500,500), random.randint(-500,500))
    x = x-1