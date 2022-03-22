from copy import deepcopy
import count
def create(inputArray):
	newArray = deepcopy(inputArray)
	for lineKey, line in enumerate(inputArray):
		for charKey, char in enumerate(line):
			if inputArray[lineKey][charKey] == "#" and count.neighbours(lineKey, charKey, inputArray) < 2:
				newArray[lineKey][charKey] = "."
			elif inputArray[lineKey][charKey] == "#" and count.neighbours(lineKey, charKey, inputArray) > 3:
				newArray[lineKey][charKey] = "."
			elif inputArray[lineKey][charKey] == "." and count.neighbours(lineKey, charKey, inputArray) == 3:
				newArray[lineKey][charKey] = "#"
			elif inputArray[lineKey][charKey] != "#" and inputArray[lineKey][charKey] != ".":
				print("Wykryto znak inny niż '#' lub '.', zamienianie na martwe komórki.")
				newArray[lineKey][charKey] = "."
	return newArray
