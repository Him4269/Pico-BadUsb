import os
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1.5)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

for x in range(5):
    layout.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.17)
    layout.send("Taskmgr.exe")
    time.sleep(0.1)