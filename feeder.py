#!/usr/bin/python3.6
##################################
#Author:mzzhmh@hotmail.com       #
##################################
import sys
debug = 0

if(len(sys.argv)!= 3):
    print("USAGE:"+sys.argv[0]+" <input data file name> <node | path>")
    print("e.g.,:"+sys.argv[0]+" Feed_data.csv node")
    sys.exit(1)

inputdata = sys.argv[1].strip()
flag = sys.argv[2].strip()

#feederFP = open('Feeder_data.csv','r')
feederFP = open(inputdata,'r')
#nodeFP = open('uniqNodes.txt','r')

if (flag == 'node'):
    connectNodeFP = open('connectNode','w')
if (flag == 'path'):
    solutionFP = open('solution','w')

#read Feeder_data.csv into a two dimension list
feederLines = feederFP.readlines() 
#inx = 0
feedDB = []
for feederLine in feederLines:
#    print(feederLine)
    tmpL = [];
    tmpL.append(feederLine.strip().split(',')[0])
    tmpL.append(feederLine.strip().split(',')[1])
    tmpL.append(feederLine.strip().split(',')[2])
    feedDB.append(tmpL)
#    print(tmpL)
if debug == 1:
    print((feedDB))
feedDB_BK = feedDB.copy()

#read uniqNode.txt into a one dimension list
#nodeLines = nodeFP.readlines()
#nodeDB = []
#for nodeLine in nodeLines:
#    nodeDB.append(nodeLine.strip())
#print(len(nodeDB))

start='1'
#build the multiple-layer map
iteration = 0
jump = 0
searchList=[]
searchList.append([start])
mapMatrix = []  #which is used for storing the map topology info
mapMatrix.append([start])

mapDist = []
mapDist.append([0])

while True:
    jump = 1
    newSearchList = []
    newDist = []
    #debug
    #for a in searchList:
    #    print(a)
    if debug == 1:
        print('searchlist')
        print(searchList)
        print('searchlist')
    for eachSearch in searchList:
        if debug == 1:
            print('es')
            print(eachSearch)
            print('es')
        tobeDel = []
        for eachElement in feedDB:
            if debug ==1:
                print('ee')
                print(eachElement)
                print('ee')
            if (eachElement.count(eachSearch[-1]) > 0):   #has next level node
                if debug == 1:
                    print('eematch')
                    print(eachElement)
                    print('eematch')
                jump = 0 #don't stop the search
                sInx = eachElement.index(eachSearch[-1]) #find if it is first node or second node
                if sInx == 0: 
                    nextNode = eachElement[1] #if first node, so next node will be the sec node
                else:
                    nextNode = eachElement[0] #if sec node, next will be first
                #add the next node into the search list and make this as an new entry in the searchList
                if debug == 1:
                    print('nn')
                    print(nextNode)
                    print('nn')
                newEachSearch = eachSearch.copy()
                newEachSearch.append(nextNode)
                if debug == 1:
                    print('nes')
                    print(newEachSearch)
                    print('nes')
                newSearchList.append(newEachSearch)
                newEachSearch = []
                tobeDel.append(eachElement)
        #delete the section information from the feedDB
        for eachDel in tobeDel:
            tmpInx = feedDB.index(eachDel)
            tmpPop = feedDB.pop(tmpInx)

    searchList = newSearchList.copy()
    mapMatrix = mapMatrix + newSearchList
    iteration = iteration + 1
    if ((jump == 1) or (iteration > 50000000)):
        #print(iteration)
        break

#print(mapMatrix)

for eachmap in mapMatrix:
    #print(flag)
    if (flag == 'node'):
        print(eachmap[-1])
        print(eachmap[-1],file=connectNodeFP)
    if (flag == 'path'):
        print(eachmap)
        print(eachmap,file=solutionFP)
#    nodeInx =  nodeDB.index(eachmap[-1])
#    nodeDB.pop(nodeInx)
#print(nodeDB)

#print(len(mapMatrix))


