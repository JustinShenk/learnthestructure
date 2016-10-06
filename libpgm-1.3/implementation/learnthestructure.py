import sys
import json
from libpgm.pgmlearner import PGMLearner

# Add to PYTHONPATH
sys.path.append("../")

# Load and clean the data
path = '../data/breastdata.txt'
f = open(path, 'r')
ftext = f.read()
ftext = ftext.translate(None, '\t\n ')
ftext = ftext.replace(':', ': ')
ftext = ftext.replace(',', ', ')
ftext = ftext.replace('None', 'null')
ftext = ftext.replace('?', '1')
data = json.loads(ftext)
newlist = []

# Convert unicode strings to int data type
for d in data:
    newlist.append(dict((k, int(v)) for k, v in d.iteritems()))

# Estimate the structure and parameters using linear guassian model
learner = PGMLearner()
resultlg = learner.lg_estimatebn(newlist)

# Print edges
print json.dumps(resultlg.E, indent=2)

# Print vertices
print json.dumps(resultlg.Vdata, indent=2)
