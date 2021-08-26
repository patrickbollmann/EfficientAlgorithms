import sys
lines = sys.stdin.readlines()
problems = int(lines[0])
lines.pop(0)


def getLength(p):  # calculate length of the result
    x = 0
    y = 0
    for j in p:
        x += len(j)
        y += 0.5
    return x/y


problem = []
subProblem = []
for line in lines:  # read inputs
    if(line == "\n"):
        if(subProblem != []):
            problem.append(subProblem)
        subProblem = []
    elif line == " \n":
        pass
    else:
        subProblem.append(line[:-1])
if(subProblem != []):  # add last subproblem if no "\n" found at the end of input
    problem.append(subProblem)


result=[]

for p in problem:  # iterate all problems
    length = getLength(p)  # get length of solution
    possibleSolutions=None
    for i in p:
        s = set()
        for j in p:
            if(len(i)+len(j)==length):
                s.add(i+j)
                s.add(j+i)
        if(possibleSolutions is None):
            possibleSolutions=s
        elif(len(possibleSolutions)==1):
            break
        else:
            possibleSolutions=possibleSolutions.intersection(s)
    result.append(str(possibleSolutions.pop()))

print("\n\n".join(result))