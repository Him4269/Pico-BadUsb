# youtube.com/technotebook
import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


time.sleep(1.5)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.1)

layout.write("notepad\n")

time.sleep(0.17)

layout.write("Your are hacked bub")
keyboard.send(Keycode.LEFT_CONTROL, Keycode.S)