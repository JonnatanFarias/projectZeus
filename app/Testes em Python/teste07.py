import pyautogui
import time
import keyboard

from pyscreeze import center

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("paint")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(208 ,381)
distance = 200
while distance>0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up







