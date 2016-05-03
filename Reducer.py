import sys
import xmltodict
import json
import glob
from collections import OrderedDict

#Cost Parameters
linehitmax = "line-hit-rate-max"
linehitmin = "line-hit-rate-min"
branch     = "branch"
time       = "time"

def myPrint(dic):
	print(json.dumps(dic, indent=1))

def getSortedSuite(directory, cost):
    suite = dict(dict())
    for filename in glob.iglob(directory):
        fd =  open(filename)
        doc = xmltodict.parse(fd.read())
        suite[filename.split("/")[-1].split(".")[0]] = doc
    
    if cost==branch:
        sortedSuite = OrderedDict(sorted(suite.items(), key=lambda k: (float((k[1]["coverage"])["@branch-rate"]))))
    else:
    	sortedSuite = OrderedDict(sorted(suite.items(), key=lambda k: (float((k[1]["coverage"])["@line-rate"]))))
    return sortedSuite

def getMinimalSetLine(sortedSuite):
	minSet = list()
	keys = list(sortedSuite.keys())
	key = keys[0]
	minSet.append(key)
	lineCoverage = list([x["coverage"]["packages"]["package"]["classes"]["class"]["lines"]["line"] for x in sortedSuite.values()])
	lines = len(lineCoverage[0])
	cases = len(lineCoverage)
	mat = list([list([int(lineCoverage[j][i]["@hits"]) for i in range(lines)]) for j in range(cases)])
	lineNumbers = list([list([int(lineCoverage[j][i]["@number"]) for i in range(lines)]) for j in range(cases)])
	linesCovered = mat[0]
	for i in range(1,cases):
		newTest = [mat[i][j]+linesCovered[j] for j in range(lines)]
		if linesCovered.count(0) > newTest.count(0):
			linesCovered = newTest
			minSet.append(keys[i])

	for i in range(cases-1,-1,-1):
		if keys[i] in minSet:
			newTest = [linesCovered[j]-mat[i][j] for j in range(lines)]
			if linesCovered.count(0) == newTest.count(0):
				linesCovered = newTest
				minSet.remove(keys[i])

	return [minSet, [lineNumbers[0][i] for i,val in enumerate(linesCovered) if val==0], lines, cases]

def getMinimalSetBranch(sortedSuite):
	minSet = list()
	keys = list(sortedSuite.keys())
	key = keys[0]
	minSet.append(key)
	branchCoverage = list([x["coverage"]["packages"]["package"]["classes"]["class"]["lines"]["line"] for x in sortedSuite.values()])
	branches = len(branchCoverage[0])
	cases = len(branchCoverage)
	mat = list([list([int(branchCoverage[j][i]["@hits"]) for i in range(branches) if branchCoverage[j][i]["@branch"]=="true"]) for j in range(cases)])
	branchNumbers = list([list([int(branchCoverage[j][i]["@number"]) for i in range(branches) if branchCoverage[j][i]["@branch"]=="true"]) for j in range(cases)])
	branchesCovered = mat[0]
	for i in range(1,cases):
		newTest = [mat[i][j]+branchesCovered[j] for j in range(branches)]
		if branchesCovered.count(0) > newTest.count(0):
			branchesCovered = newTest
			minSet.append(keys[i])

	for i in range(cases-1,-1,-1):
		if keys[i] in minSet:
			newTest = [branchesCovered[j]-mat[i][j] for j in range(branches)]
			if branchesCovered.count(0) == newTest.count(0):
				branchesCovered = newTest
				minSet.remove(keys[i])

	return [minSet, [branchNumbers[0][i] for i,val in enumerate(branchesCovered) if val==0], branches, cases]

#Main#
sortedSuite = getSortedSuite(sys.argv[1],sys.argv[2])
param = "lines"
if sys.argv[2] == branch:
	minSet = getMinimalSetBranch(sortedSuite)
	param = "branches"
else:
	minSet = getMinimalSetLine(sortedSuite)
print("Total number of ", param ," : ",minSet[2])
print("Number of ", param ," not covered : ",len(minSet[1]))
print(param ," which are not covered : ",minSet[1])
print("Total number of Test-cases : ",minSet[3])
print("Number of Test-cases selected : ",len(minSet[0]))
print("Test-cases selected : ",minSet[0])
#print(json.dumps(sortedSuite, indent=1))

