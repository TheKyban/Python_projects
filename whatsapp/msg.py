import pyautogui
import time

time.sleep(3)
# a = 0 
for i in range(100):
    # a+=1
    pyautogui.write("don't play")
    time.sleep(.4)
    pyautogui.press("Enter")
    print(i)
   