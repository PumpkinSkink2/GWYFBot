import pyautogui
import pydirectinput
import time
import win32api, win32con
import random

time.sleep(2)

# Moves the camera. Only use if you really need increments of less than 10 in the r argument.
def move(r,d): 
	if d == 'R':
		k = 1
	if d == 'L':
		k = -1
	else:
		k = 1
	win32api.mouse_event(0x0001,r*1*k, 0)

# Aims the camera more reliabliy.
def aim(r,d, delay = 0.001):
	for i in range(r):
		move(10,d)
		time.sleep(delay)

# Sets power and shoots the ball. I found that the bar has 500 values that can be incremented here. If you find it doesn't, use power_calibrate() to help you fix it.
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

#automates shooting. Is not an ambiturner. It will always turn right first, then left.
def shoot(a,p):
		aim(a,'R')
		power(p)
		aim(a,'L')

# Lets the bot detect when the next hole begins. Works similarly to the goalcheck() function.
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
# that can be used to search the "shot space". needs to use even divisors of the total number of values for angle (450) and power (500). 
# If you change those values in aim() or power() you're gonna want to change the divisors here as well.
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

		for i in range(len(anglelist)):
			for j in range(len(powerlist)):
				coordlist.append([anglelist[i],(1 + powerlist[-1-(j)])])

		return[coordlist,a_slice,p_slice]

#takes preliminary shots leading up to a search for a hole-in-one. Otherwise, the bot would just reset after every hit.
def preliminaryshots(course_coords, holenumber, moreshots, checktime = 10):
	if moreshots == 0:
		print('I do not think there are any preliminary shots to be made.')
		time.sleep(checktime)
		return

	print('I think I have to make some shots before I search for a hole in one.')
	print("I think the course_coords are" + str(course_coords))

	for k in course_coords:
		if k[2] == holenumber:
			a,p = k[0],k[1]

			shoot(a,p)
			print('I shot a preliminary shot at ' + str((a,p)))
			time.sleep(checktime)
	print('I think I am done hitting preliminary shots.')

# Will, ideally, find and return the coords for a hole in one shot to be replayed later. Should be able to handel multiple shots. Moving game geometery is another story.
def findhio(n_angle_slices, n_power_slices, preshot_list, holenumber, moreshots, checktime = 10):
	
	coord_set = []
	current_coords = []

	coord_set = gencoordlist(n_angle_slices,n_power_slices)[0]
	a_slice = gencoordlist(n_angle_slices,n_power_slices)[1]
	p_slice = gencoordlist(n_angle_slices,n_power_slices)[2]

	gotit = False

	while gotit == False:

		for i in range(n_angle_slices):
			preliminaryshots(preshot_list, holenumber, moreshots, checktime)

			current_coords=((coord_set[i][0]*a_slice),coord_set[i][1]*p_slice)
			print('current_coords = ' + str(current_coords))

			a = int((coord_set[i][0]*a_slice))
			p = int((coord_set[i][1]*p_slice))
			shoot(a,p)

			for k in range(checktime):
				if goalcheck() == True:
					gotit = True
					break
				time.sleep(1)

			if gotit == True:
				break

			reset()

		if gotit == False:
			return(None)

	print('Hole-in-one found at coordinates ' + str(current_coords) + '.')
	return(current_coords)

#Just hits the ball wildly to attempt to get a hole-in-one on the subsequent shot.
def nohio():
	wildswing = [2*random.randrange(225),500-(25*random.randrange(8))]
	# aim(wildswing[0], "R")
	# power(wildswing[1])
	return(wildswing)

# Runs the functions to learn a course and prepare a list of coordinates to run the course later. 
# Saves to a file named "name".txt where "name" is a keyword argument set in the call
def learn_course(n_angle_slices, n_power_slices, name = None, checktime = 10, holenumber = 18):
	if name == None:
		print('Please enter a name for your course replay file by using the argument "name = <filename>".')
		return

	course_coords = []
	moreshots = 0

	
	for i in range(holenumber):
		nexthole = False
		print('---------- Hole ' + str(i + 1) + ' ----------')
		while nexthole == False:

			# Checks if hole is done and waits for the next one. Also increments the holenumber.
			if nexthole == True:
				print('I think the ball is in the hole now, and am waiting for the next level')
				course_coords.append([raw_coords[0],raw_coords[1],i])
				waitfornexthole()
				breaK

			print('I think I need to search the next hole. \n' + 'course_coords = ' + str(course_coords))

			# Runs the search function and attempts to return the coords that it did so at. If not it returns None.

			raw_coords = findhio(n_angle_slices,n_power_slices, course_coords, i, moreshots)
			print('raw_coords = ' + str(raw_coords))

			

			if goalcheck() == True:
				course_coords.append([raw_coords[0],raw_coords[1],i])
				waitfornexthole()
				nexthole = True

			# Appends a wildswing() call's coords to the coord list with the current hole number. Allows for maps that lack a hio to be completed.
			if nexthole == False:

				print('No hole-in-one found. Adding an additional shot.')
				raw_coords = nohio()
				course_coords.append([raw_coords[0],raw_coords[1],i])
				moreshots = moreshots+1

				print('moreshots = ' + str(moreshots))
				print('course_coords (after) = ' + str(course_coords))

			

	# Saves the completely "learned" course.
	savereplay = open(name + '.txt', 'w')
	savereplay.write(str(course_coords))
	savereplay.close()

# Loads replay file and outputs a 2 dimensional list (a list of lists of form [[angle,power,holehumber],[angle,power,holehumber],...]) of the coordinates to replay a course.
def parsereplay(loadreplay):
	coord_list = []
	coord_triplet = []

	#takes the replay file as a string, and converts it into a list of values.
	raw_coord_list = (loadreplay.readline())
	raw_coord_list = raw_coord_list.replace('[','')
	raw_coord_list = raw_coord_list.replace(']','')
	raw_coord_list = raw_coord_list.replace(' ','')
	raw_coord_list = raw_coord_list.split(',')
	for i in range(len(raw_coord_list)):
		raw_coord_list[i] = float(raw_coord_list[i])
		raw_coord_list[i] = int(raw_coord_list[i])

	#Uses some known information about the format of the file (each entry should be 3 numbers long) to break the list up into coordinate sets of form [angle,power,holenumber]
	for n in range(int((len(raw_coord_list)/3))):
		i,j,k = (0+(3*n)),(1+(3*n)),(2+(3*n))

		coord_triplet.append(int(raw_coord_list[i]))
		coord_triplet.append(int(raw_coord_list[j]))
		coord_triplet.append(int(raw_coord_list[k]))

		coord_list.append(coord_triplet)
		coord_triplet = []
	return(coord_list)

# Counts the number of holes in a replay list. 
# Uses the third value in a coordinate list of form [angle,power,holehumber] to determine the number of holes.
def holecounter(coord_list):

	holecounter = []
	
	for i in coord_list:
		if (i[2]) not in (holecounter):
			holecounter.append(i[2])
			holenumber = len(holecounter)
	return(holenumber)

# Counts the number of shots in a hole for each hole on a course. 
# Takes a list of the full coordinates for a course in form [[angle,power,holehumber],[angle,power,holehumber],...], and the number of holes on a course as arguments.
def shotcounter(coord_list, holenumber):
	shotcount_list = []
	for i in range(holenumber):
		shotcount = 0

		for j in coord_list:
			if j[2] != i:
				pass
			else:
				shotcount = shotcount+1
		shotcount_list.append(shotcount)
	return(shotcount_list)

# Replays a course using the full coordinates for a course in form [[angle,power,holehumber],[angle,power,holehumber],...], 
# the number of holes on a course, and a list of the number of shots on each hole as arguments. 
# Has a "checktime" kwarg that allows to adjust how long it checks for a completed course in after shooting.
def replaycourse(coord_list, holenumber, shotcount_list, checktime = 10):
	for i in range(holenumber):
		print('---------- Hole ' + str(i + 1) + ' ----------')
		hole_list = []
		for k in coord_list:
			if k[2] == i:
				hole_list.append(k[0])
				hole_list.append(k[1])

		active_coords = hole_list
		for j in range(shotcount_list[i]):
			x,y = 2*int(j), 2*int(j)+1
			a,p = active_coords[x], active_coords[y]
			print('(Angle, Power) = ' + str((a,p)))
			shoot(a,p)

		for k in range(checktime):
			print('Checking...')
			if goalcheck() == True:
				print('I appear to have gotten the ball in')
				print("I'm waiting for the next hole.")
				waitfornexthole()
				time.sleep(3)
				break
			time.sleep(1)

# loads a replay file of the name called using "name = 'name'", and plays it.
def replay(name = None, checktime = 10):

	shotcount_list = []
	hole_list = []
	meta_list = []

	if name == None:
		print('you need to put in the name for the replay file.')
		return

	with (open(str(name) + '.txt', 'r')) as loadreplay:

		shotnumber = None
		holenumber = None
		coord_list = []

		#reads txt file to a list of shot coords and which hole they occur on.
		coord_list = parsereplay(loadreplay)

		#counts the number of holes in the presented list
		print(coord_list)
		holenumber = holecounter(coord_list)

		## counts the number of shots in a hole
		shotcount_list = shotcounter(coord_list,holenumber)

		# does the heavy lifting of automating the course.
		replaycourse(coord_list, holenumber, shotcount_list)				
