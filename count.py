def neighbours(y, x, inputArray):
	counter = 0
	try:
		if x-1 >= 0 and y-1 >= 0 and inputArray[y-1][x-1] == "#":
			counter += 1
	except:
		pass
	try:
		if x >= 0 and y-1 >= 0 and inputArray[y-1][x] == "#":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y-1 >= 0 and inputArray[y-1][x+1] == "#":
			counter += 1
	except:
		pass
	try:
		if x-1 >= 0 and y >= 0 and inputArray[y][x-1] == "#":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y >= 0 and inputArray[y][x+1] == "#":
			counter += 1
	except:
		pass
	try:
		if x-1 >= 0 and y+1 >= 0 and inputArray[y+1][x-1] == "#":
			counter += 1
	except:
		pass
	try:
		if x >= 0 and y+1 >= 0 and inputArray[y+1][x] == "#":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y+1 >= 0 and inputArray[y+1][x+1] == "#":
			counter += 1
	except:
		pass
	return counter 
