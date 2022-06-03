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
	# originally it was a tool to help calibrate the number of "mickeys" 
	# the mouse needs to move to do 1 full rotation (it was 450 for me). 
	# now it functions as a better version of the old aim function. it is more consistent.
def aim(r,d, delay = 0.001):
	for i in range(r):
		move(10,d)
		time.sleep(delay)

#sets power and shoots the ball. I found that the bar has 500 values that can be incremented here. 
def power(p, noshot = False, delay = 1):
	win32api.mouse_event(0x0002,0,0)
	win32api.mouse_event(0x0001,0,(-1*p))

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
	# and set just sets the power to a specified value.
def power_calibrate(num, n = 10 ,stepsize = 10, mode = 'set', delay = 1):
		
		if mode == 'decrease':
			for i in range(n):
				print(i)
				power((500-(stepsize*i)), noshot = True, delay = delay)

		if mode == 'increase':
			for i in range(n):
				print(i)
				power((num+(stepsize*i)), noshot = True, delay = delay)
		if mode == 'set':
			power(num, noshot = True, delay = delay) 	

#resets the ball.
def reset():
	pydirectinput.press('r')

# Lets the bot detect when the next hole begins.
def waitfornexthole():
	g = False
	px = pyautogui.pixel(543,988)

	# print(px)
	while px != (99,200,121):
		time.sleep(1)
		px = pyautogui.pixel(543,988)
	else:
		print('The next hole has started!')
		g = True
		return (g)

# Decides if the ball went in the hole. Best if run while the bot is waiting after hitting the ball.
# Returns "True" if the ball goes in the hole. 
# Works based off of pixel color recognition from the power meter in the bottom left
def goalcheck():
	g = False
	px = pyautogui.pixel(543,988)

	# print(px)
	if px != (99,200,121):
		print('Got it!')
		g = True
		return (g)

# takes a number of angle, power slice to be searched and outputs a list of coordinates
# that can be used to search the "shot space".
def gencoordlist(n_angle_slices, n_power_slices):

	a_divisors = [1, 2, 3, 5, 6, 9, 10, 15, 18, 25, 30, 45, 50, 75, 90, 150, 225, 450]
	p_divisors = [1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250,500]
	
	anglelist = []
	powerlist = []
	coordlist = []

	if n_angle_slices not in a_divisors or n_power_slices not in p_divisors:
		print('You should use divisors of the number of rotational and power increments. ' +
			  'For angle pick from ' + str(a_divisors) + ', ' + 'and for power pick from ' + str(p_divisors))

	else:
		a_slice = 450/n_angle_slices
		for i in range(n_angle_slices):
			anglelist.append(i)

		p_slice = 500/n_power_slices
		for i in (range(n_power_slices)):
			powerlist.append(i)

		# print(str(anglelist) + '\n ffffffffffffffffffffffff \n' + str(powerlist))

		for i in range(len(anglelist)):
			for j in range(len(powerlist)):
				coordlist.append([anglelist[i],(1 + powerlist[-1-(j)])])

		return[coordlist,a_slice,p_slice]
	
	# print (n_angle_slices, n_power_slices)

#runs the bot. Will, ideally, find and return the coords for a hole in one shot to be replayed later.
def findhio(n_angle_slices, n_power_slices, checktime = 5):
	coord_set = []
	coord_set = gencoordlist(n_angle_slices,n_power_slices)[0]
	a_slice = gencoordlist(n_angle_slices,n_power_slices)[1]
	p_slice = gencoordlist(n_angle_slices,n_power_slices)[2]

	for i in range(n_angle_slices):

		if goalcheck() == True:
			print('Hole-in-one found at coordinates ' + str(current_coords) + '.')
			return(current_coords)

		current_coords=((coord_set[i][0]*a_slice),coord_set[i][1]*p_slice)
		print(current_coords)

		aim(int((coord_set[i][0]*a_slice)),'R')
		power(int((coord_set[i][1]*p_slice)))
		aim(int((coord_set[i][0]*a_slice)),'L')
		for k in range(checktime):
			if goalcheck() == True:
				print(current_coords)
				break
			time.sleep(1)
		reset()

# Runs the functions to learn a course and prepare a list of coordinates to run the course later. 
# Saves to a file named "name".txt where "name" is a keyword argument set in the call
def learn_course(n_angle_slices, n_power_slices, name = None, checktime = 5, holenumber = 18):
	if name == None:
		print('Please enter a name for your course replay file by using the argument "name = <filename>".')
		return
	course_coords = []
	for i in range(holenumber):
		course_coords.append(findhio(n_angle_slices,n_power_slices, checktime = checktime))
		waitfornexthole()

		print(course_coords)
	savereplay = open(name + '.txt', 'w')
	savereplay.write(str(course_coords))
	savereplay.close()

