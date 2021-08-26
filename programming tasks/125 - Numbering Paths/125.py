import sys
lines = sys.stdin.readlines()   #read Input
#-----clean input----
tmp=[]
clean=[]
for line in lines:
    numbers=line.split(" ")
    for q in numbers:
        tmp.append(q)
for e in tmp:
    if(e != "\n"):
        clean.append(e)
        

#------
count=0 #set counter for problems to 0

def getMatrix(streets, numberOfStreets):
    if(numberOfStreets == 0):   #case: 0 streets
        return []

    city =[]
    temp =[]

    for street in streets:
        temp.append(street[0])
        temp.append(street[1])
    dim = max(temp)+1  #get dimension of city matrix

    for i in range(dim):    #initialize city matrix
        r=[]
        for j in range(dim):
            r.append(0)
        city.append(r)
    for i  in range(len(streets)):  #set number of streets =1 for given streets
        street=streets[i]
        city[street[0]][street[1]]+=1


    #--- Floyd Warshall -- use modified floyd warshall algorithm to calculate number of paths using multiple crosses

    for k in range(dim):
        for i in range(dim):
            for j in range(dim):
                 city[i][j]+=city[i][k]*city[k][j]

    #search for loops, set values to -1
    for k in range(dim):
        if(city[k][k]):
            for i in range(dim):
                for j in range(dim):
                    if(city[i][k]and city[k][j]):
                        city[i][j]=-1

    return city


while(len(clean)>0):

#--- get streets from clean input
    numberOfStreets=int(clean.pop(0))
    streets=[]
    for i in range(numberOfStreets):   #get all streets
        x = int(clean.pop(0))
        y = int(clean.pop(0))
        streets.append([x,y])
#-----

    city=getMatrix(streets, numberOfStreets)

    #-- Print city matrix
    print("matrix for city "+str(count))
    for row in city:
        print(" ".join(str(x) for x in row))
    count+=1