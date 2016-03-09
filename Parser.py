import untangle
import sys
import xmltodict
import pprint
import json
pp = pprint.PrettyPrinter(indent=4)
with open(sys.argv[1]) as fd:
    doc = xmltodict.parse(fd.read())
print(json.dumps(doc, indent=4))
