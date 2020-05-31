# Author - Rakshat Kashyap
# This bot plays piano tiles 2 game on its on all you need to do is run it
# ENJOY>>>


#Importing required libraries, you need to install keyboard, win32api and mss using pip command
import time
import keyboard
import win32api, win32con
from mss import mss


# defining the start area of the tiles, it can be different for you so use pyautogui.displayMousePosition() function to get coords on your screen, pyautogui is and external library

startX =975
startY =920
coords = (0,200,400,599) # this is the space between each row

# function to click at a given coordinate
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

sct = mss()

# function to check if there is a tile to be clicked
def start(txx):
	img = sct.grab((975,920,1575,921))  # gets the screenshot of the area to be checked
	for coord in coords:
		if img.pixel(coord,0)[0] < 100:  # checks if the area has any clickable tile i.e. checks if it is blue or black
			if txx<180:                     # configuration when speed gets high
				click(startX+coord,startY+100)
			else:
				click(startX+coord,startY+150)

t = time.time()
while keyboard.is_pressed('q') == False:  # this is a failsafe press (q) when you want to stop the program
	tx = t-time.time()
	start(tx)


