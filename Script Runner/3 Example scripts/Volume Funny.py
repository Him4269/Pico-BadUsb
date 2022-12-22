# youtube.com/technotebook
import time
import os
import random
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl

time.sleep(1.5)

CC = ConsumerControl(usb_hid.devices)
for x in range(5):
    for x in range(50):
        CC.send(0xEA)
    for x in range(50):
        CC.send(0xE9)