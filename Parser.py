import sys
import xmltodict
import json
import glob

def getSortedSuite(directory):
    suite = dict(dict())
    for filename in glob.iglob(directory):
        fd =  open(filename)
        doc = xmltodict.parse(fd.read())
        suite[filename.split("/")[-1].split(".")[0]] = doc
    
    sortedSuite = sorted(suite.values(), key=lambda k: (float((k["coverage"])["@branch-rate"])))
    return sortedSuite

def getMinimalSet(sortedSuite):
	minSet = list()
	lineCoverage = 
#Main#
directory = "xml/test/*"
sortedSuite = getSortedSuite(directory)
print(json.dumps(sortedSuite, indent=1))