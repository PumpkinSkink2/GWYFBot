# What need do:
# 1.see course, find flagpole... maybe
# 2.aim camera
# 3.set power
# 4.did ball go in?
# 	if not, repeat above.

import pyautogui
import pydirectinput
import time
import win32api, win32con
import random

time.sleep(2)

#moves the camera
def move(r,d): 
	if d == 'R':
		k = 1
	if d == 'L':
		k = -1
	else:
		k = 1
	win32api.mouse_event(0x0001,r*1*k, 0)

#aims the camera
	# originally it was a tool to help calibrate the number or "mickeys" 
	# the mouse needs to move to do 1 full rotation.
	# (it was 450 for me). 
	# now it functions as a better version of the old aim function. it is more consistent.
def aim(r,d, delay = 0.001):
	print(r)
	for i in range(r):
		
		move(10,d)
		time.sleep(delay)

#sets power and shoots the ball
def power(p, noshot = False, delay = 1):
	win32api.mouse_event(0x0002,0,0)
	win32api.mouse_event(0x0001,0,-1*p)

	time.sleep(delay)

	if noshot == False:
		win32api.mouse_event(0x0004,0,0)

	if noshot == True:
		time.sleep(delay)
		win32api.mouse_event(0x0001,0,1*p)
		time.sleep(delay)

# debug tool to help calibrate the power bar. 
# decrease decreases the power level by a set increment, 
# increase increases from 1 at a set increment, 
# and set just sets teh power to a specified value.

def power_calibrate(num, n = 10 ,stepsize = 10, mode = 'decrease', delay = 1):
		
		if mode == 'decrease':
			for i in range(n):
				print(i)
				power((512-(stepsize*i)), noshot = True, delay = delay)

		if mode == 'increase':
			for i in range(n):
				print(i)
				power((num+(stepsize*i)), noshot = True, delay = delay)
		if mode == 'set':
			print(i)
			power(num, noshot = True, delay = delay) 	

#resets the ball.
def reset():
	pydirectinput.press('r')

#decides if the ball went in the hole, t is the number of seconds to check for. Best if run while the bot is waiting after hitting the ball.
def goalcheck(t):
	g = False
	
	if g == True:
		time.sleep(10-m)
		print('this worked')
		return(g)

	for n in range(t):
		px = pyautogui.pixel(543,988)
		# print(px)
		if px != (99,200,121):
			print('Got it!')
			g = True
			m = n
			break
		else:
			time.sleep(1)
	return (g)
