import math
import numpy

startingConfig=numpy.array(([1,2,3,4],[5,6,7,8],[9,10,11,12],[15,14,13,0]), dtype=int)
goalConfig=numpy.array(([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]), dtype=int)
M=4




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





#print startingConfig
#print goalConfig
#print MisplacedTileD(startingConfig)
print ManhattanD(startingConfig)