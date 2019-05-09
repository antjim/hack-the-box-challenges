#AORA

import sys
import os
import base64

key = range(37)

path = sys.argv[1]
folders = os.listdir(path)

for f in folders:
	files = os.listdir(path+"/"+f)
	for file in files:
		key[int(file)] = str(f.split("-")[0])


encoded_key = (' '.join(str(x) for x in key)).replace(" ","")

print(base64.b64decode(encoded_key[1:]))

