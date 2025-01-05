import pyautogui
import time

#clicks skip button even when the screen is different sizes

print('**running**')
while True:
	time.sleep(1)
  #get an image (cropped screenshot of skip button) put in same folder as py script, or don't.  whatever you want
	skip_location = pyautogui.locateOnScreen('skip_button.png',confidence=0.5)
	if skip_location:
		print(skip_location) 
		skip_location_point = pyautogui.center(skip_location)
		skip_locationx,skip_locationy = skip_location_point
		pyautogui.click(skip_locationx,skip_locationy)
