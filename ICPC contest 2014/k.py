import sys
from operator import itemgetter

#lines = sys.stdin.readlines()  # lese Input
file = open("test2.in")
lines=file.readlines()


def floydWarshallMin(graph,v):
    for k in range(0,v):
        for i in range(0,v):
            for j in range(0,v):
                if(graph[i][j] > graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
    min =99999
    for i in range(0,v):
        if(graph[i][i]<min):
            min = graph[i][i]
    return min


def solve(lines):
    first = lines.pop(0).split(" ")
    #print(first)
    length = int(first[0])
    n = int(first[1])
    covers = []
    one = 0

    for line in lines:
        line = line.replace('\n', '')
        #print(line)
        line = line.split(" ")
        #print(line)
        x=int(line[0])
        y=int(line[1])
        if(x==y+1):
            return 1
        overlap=0
        for cover in covers:
            if(x<y):
                if(cover[0]<=x and cover[1]>=y):
                    overlap=1
                    break
            if(x>y):
                if(cover[0]>=x and cover[1]<=y):
                    overlap=1
                    break
        if(overlap==1):
            pass
        else:
            covers.append([x,y])
        

    covers.sort(key=itemgetter(1))

    #print(length)
    ##print(n)
    #print(covers)

    matrix = [[99999] * len(covers) for j in range(len(covers))]

    #print(matrix)

    for i in range(len(covers)):
        for j in range(len(covers)):
            if(i == j):
                if(covers[i][0]==1 and covers[i][1]==length):
                    matrix[i][j] = 1
                if(covers[i][0]==covers[i][1]+1):
                    matrix[i][j] = 1
            elif(j>i or covers[j][0] > covers[j][1]):
                if(covers[i][1] >= covers[j][0]-1):
                    matrix[i][j] = 1
            elif(covers[i][1] == length and covers[j][0]==1):
                matrix[i][j] = 1
            if(i<j and covers[i][0] > covers[i][1] and covers[j][0] > covers[j][1]):
                #print("test")
                if(covers[i][1] >= 1):
                    matrix[i][j] = 1

    #for i in range(n):
    #    print(matrix[i])
    #rint(covers)
    res=(floydWarshallMin(matrix,len(covers)))
    if(one==1):
        res=1
    if(res<99999):
        return(res)
    else:
        return("impossible")

print(solve(lines))