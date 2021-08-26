import sys

def checkH(x,y,length): #prüfe ob eine horizontale Kante eines potentiellenQuadrates mit länge 'length' existiert
    res=0
    for i in range (length):
        if([x,y+i] in horizontal):
            pass
        else:
            return False
    return True
def checkV(x,y,length): #prüfe ob eine vertikale Kante eines potentiellenQuadrates mit länge 'length' existiert
    res=0
    for i in range (length):
        if([x,y+i] in vertical):
            pass
        else:
            return False
    return True
def searchSquares(n,horizontal,vertical):
    solved=False
    squares=0
    for size in range(1,n+1):   #alle möglichen Größen eines Quadrates
        for i in range(n): # gehe über alle reihen
            for j in range (n): #gehe über alle Spalten
                if(checkH(i,j,size) and checkH(i+size,j,size) and checkV(j,i,size) and checkV(j+size,i,size)): #teste ob alle 4 Seiten des Quadrates existieren
                    squares +=1
                    solved=True
                    #print("found square at:"+str(i)+", "+str(j))
        if(squares>0):
            print(str(squares)+" square (s) of size "+str(size))
        squares=0
    if(solved==False):
        print("No completed squares can be found.")
        
try:
    lines = sys.stdin.readlines()   #lese Input

    start=0
    p=1
    while(start<len(lines)-1):
        n=int(lines[start])
        m=int(lines[start+1])
        horizontal =[]
        vertical=[]
        for i in range(start+2,m+start+2):  #erstelle listen für horizontale und vertikale linien
            if(lines[i][0]=="H"):
                horizontal.append([int(lines[i][2]),int(lines[i][4])])
            if(lines[i][0]=="V"):
                vertical.append([int(lines[i][2]),int(lines[i][4])])
        
        if(p!=1):
            print("\n**********************************\n")
        print("Problem #"+str(p)+"\n")
        searchSquares(n,horizontal,vertical)    #suche Quadrate für das aktuelle Problem
        start=start+m+2 #springe zum Start des nächsten Problems
        p=p+1
except Exception as e:
    print(e)