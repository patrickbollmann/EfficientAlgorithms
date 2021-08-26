import sys
import math
# --- Read Inputs
x = []
y = []
lines = sys.stdin.readlines()
first = lines.pop(0)
amount = int(first[:-1])
for line in lines:
    line = line.replace('\n', '')
    line = line.split()
    x.append(int(line[0]))
    y.append(int(line[1]))
cx = 0
area = 0
grounds = []
for i in range(len(x)):
    if(y[i] == 0):
        grounds.append(x[i])

# --Split Polygon into triangles and calc area
for i in range(len(x)):
    # Split Polygon into triangles and calc area
    Triangle = (1/2)(x[i-1]*y[i] - x[i]*y[i-1])    #https://en.wikipedia.org/wiki/Shoelace_formula
    area += Triangle
    cx += (x[i-1]+x[i])*Triangle  #https://en.wikipedia.org/wiki/Centroid
cx = cx/(3*area)
area = abs(area)    #area might be negative depending on where we start - fix

minx = min(grounds)
maxx = max(grounds)

# trivial cases:
# center off the left and weight also off the left or at left foot
if(cx < minx and x[0] <= minx):
    #print("center off the left and weight also off the left")
    print("unstable")
# center off the right and weight also off the right or at right foot
elif(cx > maxx and x[0] >= maxx):
    #print("center off the right and weight also off the right")
    print("unstable")
# center is between feet and weight is also between feet
elif(cx >= minx and cx <= maxx and x[0] >= minx and x[0] <= maxx):
    #print("center is between feet and weight is also between feet")
    print("0 .. inf")

# real cases:
else:
    if(cx > minx and cx < maxx):  # center between feet of crane
        #print("center between feet of crane")
        if (x[0] > maxx):  # weight hanging off the right side
            maxw = (maxx - cx)/(x[0] - maxx)*area
            # print(cx)
            if(maxw > 0):
                # print(maxw)
                print("0 .. "+str(math.ceil(maxw)))
            else:
                print("unstable")

        else:  # weight hanging off the left side

            maxw = (cx-minx)/(minx - x[0])*area
            if(maxw > 0):
                print("0 .. "+str(math.ceil(maxw)))
            else:
                print("unstable")

    elif(cx > maxx):  # center is off the right
        #print("center is off the right")
        if(x[0] < minx):  # weight hanging off the left
            minw = (cx - maxx)/(maxx-x[0])*area
            maxw = (cx - minx)/(minx - x[0])*area
            print(str(math.floor(minw))+" .. "+str(math.ceil(maxw)))
        else:  # weight not off the left
            maxw = (cx - maxx)/(maxx-x[0])*area
            print(str(math.floor(maxw))+" .. inf")

    elif(cx < minx):  # center is off the left
        #print("center is off the left")
        if(x[0] > maxx):  # weight hanging off the right
            minw = (minx - cx)/(x[0]-minx)*area
            maxw = (maxx - cx)/(x[0] - maxx)*area
            print(str(math.floor(minw))+" .. "+str(math.ceil(maxw)))
        else:  # weight not off the right
            maxw = (minx - cx)/(x[0]-minx)*area
            print(str(math.floor(maxw))+" .. inf")
