import sys
import math

lines = sys.stdin.readlines()
numberOfTestCases = int(lines[0])
lines.pop(0)

for i in range(numberOfTestCases):
    numberOfPeople= int(lines[0].split(" ", 2)[2])

    lines.pop(0)
    xcoords = list()
    ycoords = list()
    for j in range(numberOfPeople):
        line = lines.pop(0)
        pos = line.split(" ",1)
        xcoords.append(int(pos[0]))
        ycoords.append(int(pos[1]))

    xcoords.sort()
    ycoords.sort()
    street = xcoords[math.ceil(numberOfPeople/2-1)]
    avenue = ycoords[math.ceil(numberOfPeople/2-1)]
    print("(Street: "+ str(street)+ ", Avenue: "+ str(avenue)+ ")")