from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

time.sleep(10)
keyboard.press(Key.right)

keyboard.release(Key.right)

