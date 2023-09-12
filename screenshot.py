#!/usr/bin/env python

from pynput import keyboard
from PIL import ImageGrab

ctrl_mode = False
screenshot_name = "page"
screenshot_idx = 0


def on_key_release(key):
    global ctrl_mode
    global screenshot_idx
    global screenshot_name

    try:
        if key == keyboard.Key.ctrl_l:
            ctrl_mode = True
        elif ctrl_mode and key.char == 'm':
            ctrl_mode = False
            screenshot = ImageGrab.grab()
            image_name = screenshot_name + str(screenshot_idx) + '.png'
            screenshot.save(image_name)
            screenshot_idx = screenshot_idx+1
            print(f'Screenshot saved as ${image_name}.png')
        else:
            ctrl_mode = False
    except AttributeError:
        pass


listener = keyboard.Listener(on_release=on_key_release)
listener.start()
listener.join()
