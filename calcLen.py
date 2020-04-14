#!/usr/bin/python3.6
##################################
#Author:mzzhmh@hotmail.com       #
##################################
import json
import ast
import sys
import os
#find distance of one section in feedDB
def findDist(fst,snd,db):
    dist = None
    DBlen = len(db)
    i = 0
    for i in range(DBlen):
        if ((fst in db[i]) and (snd in db[i])):
            dist = db[i][2]  #record distance
            break
    if(dist == None):
        print("ERROR: NO DIST found for this Section")
        print(fst)
        print(snd)
        print("=====================================")
        sys.exit(1)
    else:
        return(float(dist))

if(len(sys.argv)!= 3):
    print("USAGE:"+sys.argv[0]+" <input data file name> <sum | path>")
    print("e.g.,:"+sys.argv[0]+" Feed_data.csv sum")
    sys.exit(1)

inputdata = sys.argv[1].strip()
flag = sys.argv[2].strip()

if(os.stat('solution').st_size == 0):
    print("'solution' file is empty. You need to run './feeder.py <input CSV file> path' first!")
    sys.exit(1)

feederFP = open(inputdata,'r')
resFP = open('solution','r')

if(flag == 'sum'):
    solutionLenSumFP = open('solutionLenSum','w')
if(flag == 'path'):
    solutionLenFP = open('solutionLen','w')

resLines = resFP.readlines()
feederLines = feederFP.readlines()

feedDB = []
for feederLine in feederLines:
#    print(feederLine)
    tmpL = [];
    tmpL.append(feederLine.strip().split(',')[0])
    tmpL.append(feederLine.strip().split(',')[1])
    tmpL.append(feederLine.strip().split(',')[2])
    feedDB.append(tmpL)
#print((feedDB))

mapDist = [[0]]

for resLine in resLines:
    #print((resLine.strip()))
    resLineList = ast.literal_eval(resLine.strip())
    entryLen = len(resLineList)
    #print(entryLen)
    if entryLen>1:
        st = 0
        eachDist=[]
        for st in range(entryLen-1):
            first = resLineList[st]
            second = resLineList[st+1]
            #find distance of this section
            sectionDist = findDist(first,second,feedDB)
            eachDist.append(sectionDist)
            st = st + 1
            #eachDist.append(1)
        mapDist.append(eachDist)

for eachMap in mapDist:
    if(flag == 'path'):
        print(eachMap)
        print(eachMap,file=solutionLenFP)
    if(flag == 'sum'):
        print(sum(eachMap))
        print(sum(eachMap),file=solutionLenSumFP)


