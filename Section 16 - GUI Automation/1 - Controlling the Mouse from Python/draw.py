import pyautogui

pyautogui.moveTo(600, 530)
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance -= 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance -= 25
    print(0, distance)
    pyautogui.dragRel(0, -distance, duration=0.1)
