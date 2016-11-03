import math
import numpy


startingConfig=numpy.array(([1,2,3,4],[5,6,7,8],[9,10,11,12],[15,14,13,0]), dtype=int)
goalConfig=numpy.array(([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]), dtype=int)
queue=[]

iterations=0
maxdepth=0
tuple=(startingConfig,0)
queue.append(tuple)
M=4
current=0



def MisplacedTileD(currentArray):
    difference=0
    goal = numpy.nditer(goalConfig, flags=['f_index'])
    current = numpy.nditer(currentArray, flags=['f_index'])
    while not goal.finished:
        if (goal[0]!=current[0]):
            difference+=1
        goal.iternext()
        current.iternext()
    return difference

def ManhattanD(currentArray):
    difference=0
    for i in range(0,M,1):
        for j in range (0,M,1):
            if currentArray[i][j]==0:
                continue
            goalI=(currentArray[i][j]-1)/M
            goalJ=(currentArray[i][j]-1)%M
            if goalI!=i or goalJ!=j:
                difference+=abs(goalI-i)+abs(goalJ-j)
    return difference

while True:
    if queue.__sizeof__()>maxdepth:
        maxdepth=queue.__sizeof__()
    queue.sort(key=lambda tup: tup[1])
    current=queue.pop()[0]
    if current==goalConfig:
        break
    zI=numpy.where(startingConfig==0)[0][0]
    zJ=numpy.where(startingConfig==0)[1][0]
    if(zI>0):
        temp=current
    if(zI<M-1):

    if(zJ>0):

    if(zJ<M-1):





#print startingConfig
#print goalConfig
#print MisplacedTileD(startingConfig)
#print ManhattanD(startingConfig)
