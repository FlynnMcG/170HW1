import math
import numpy


startingConfig=numpy.array(([1,2,3],[4,8,0],[7,6,5]), dtype=int)
goalConfig=numpy.array(([1,2,3],[4,5,6],[7,8,0]), dtype=int)
queue=[]

iterations=0
maxsize=0
tuple=(startingConfig,0,0,hash(startingConfig.tostring()))
queue.append(tuple)
M=3
current=0
deadQueue=[]


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
                # print currentArray[i][j]
                difference+=abs(goalI-i)+abs(goalJ-j)
    #             print "Difference="
    #             print difference
    # print "Restart"
    return difference


while True:
    if len(queue)>maxsize:
        maxsize=len(queue)

    queue.sort(key=lambda tup: -tup[3])
    prev = 0
    counter = 0
    for i in queue:
        if i[3] == prev:
            del queue[counter]
        else:
            counter = counter + 1
        prev = i[3]
    queue.sort(key=lambda tup: -tup[1])
    current=queue.pop()
    dead=(current[2],current[3])
    deadQueue.append(dead)
    # print current[1]
    depth=current[2]+1

    current=current[0]
    print current
    if numpy.array_equal(current,goalConfig):
        break
    zI=numpy.where(current==0)[0][0]
    zJ=numpy.where(current==0)[1][0]
    if(zI>0):
        temp=numpy.copy(current)
        temp[zI][zJ],temp[zI-1][zJ]=temp[zI-1][zJ],temp[zI][zJ]
        temp=(temp,ManhattanD(temp)+depth,depth, hash(temp.tostring()))
        checker=[i for i, v in enumerate(deadQueue) if v[1] == temp[3]]
        if len(checker)>0:
            if depth>=deadQueue[checker[0]][0]:
                depth=depth
            else:
                deadQueue[checker][0]=depth
                queue.append(temp)
        else:
            queue.append(temp)

        # print "up"
        # print temp
    if(zI<M-1):
        temp = numpy.copy(current)
        temp[zI][zJ], temp[zI + 1][zJ] = temp[zI + 1][zJ], temp[zI][zJ]
        temp = (temp, ManhattanD(temp) + depth, depth, hash(temp.tostring()))
        checker = [i for i, v in enumerate(deadQueue) if v[1] == temp[3]]
        if len(checker) > 0:
            if depth >= deadQueue[checker[0]][0]:
                depth = depth
            else:
                deadQueue[checker][0] = depth
                queue.append(temp)
        else:
            queue.append(temp)
        # print "down"
        # print temp
    if(zJ>0):

        temp = numpy.copy(current)
        temp[zI][zJ], temp[zI][zJ-1] = temp[zI][zJ-1], temp[zI][zJ]
        temp = (temp, ManhattanD(temp) + depth, depth, hash(temp.tostring()))
        checker = [i for i, v in enumerate(deadQueue) if v[1] == temp[3]]
        if len(checker) > 0:
            if depth >= deadQueue[checker[0]][0]:
                depth = depth
            else:
                deadQueue[checker][0] = depth
                queue.append(temp)
        else:
            queue.append(temp)
        # print "left"
        # print temp
    if(zJ<M-1):
        temp = numpy.copy(current)
        temp[zI][zJ], temp[zI][zJ+1] = temp[zI][zJ+1], temp[zI][zJ]
        temp = (temp, ManhattanD(temp) + depth, depth, hash(temp.tostring()))
        checker = [i for i, v in enumerate(deadQueue) if v[1] == temp[3]]
        if len(checker) > 0:
            if depth >= deadQueue[checker[0]][0]:
                depth = depth
            else:
                deadQueue[checker][0] = depth
                queue.append(temp)
        else:
            queue.append(temp)
        # print "right"
        # print temp



print maxsize
print depth
print current
