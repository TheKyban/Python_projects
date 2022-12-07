import pyautogui
import time

time.sleep(3)
# Unlimited
a = 0 
while True:
    a+=1
    pyautogui.write("Hello")
    time.sleep(.5)
    pyautogui.press("Enter")
    print(a)
   