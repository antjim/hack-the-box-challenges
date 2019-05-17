import cPickle as pickle
import sys

filePath = sys.argv[1]

f = open(filePath,"rb")

result = pickle.load(f)

for ary in result:
	line=""
	for tup in ary:
		line += tup[0] * tup[1]
	print(line)