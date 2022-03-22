import sys
import nextGen

f = open("gameoflife.txt")


input = f.read().splitlines()

global inputArray
inputArray = []	
for line in input:
	inputArray.append(list(line))


def gameOfLife(gameArray, gen):
    newArray = nextGen.create(gameArray)
    with open(f"gen{gen+1}.txt", "w") as f:
        for line in newArray:
            f.write(" ".join(line) + "\n")
    gameArray = newArray
    return gameArray


if int(sys.argv[1]) > 0:
    for i in range(int(sys.argv[1])):
        inputArray = gameOfLife(inputArray,i)
else:
    print("Liczba generacji jest niepoprawna, wprowadź wartość większą od 0")
