import pyautogui
import random

width, height = pyautogui.size()

print(width, height)

for i in range(1, 6):
    pyautogui.moveTo(random.randint(1, width), random.randint(1, height), duration=0.5)
    print(i, pyautogui.position())

pyautogui.moveTo(960, 540, duration=0.5)
print()

for i in range(1, 6):
    pyautogui.moveRel(random.randint(-100, 100), random.randint(-100, 100), duration=0.5)
    print(i, pyautogui.position())

pyautogui.click(601, 1057, duration=0.5)
pyautogui.click(601, 1057, duration=0.5)

# pyautogui.displayMousePosition() !!! Only run this in a terminal! Live position of cursor !!!
