from pyautogui import leftClick
import time
from pynput.mouse import Button, Controller

time.sleep(10)
for c in range(2, 150000):

 mouse = Controller()
 mouse.click(Button.left, 500)
