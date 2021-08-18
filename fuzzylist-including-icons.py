#!/usr/bin/python

from __future__ import print_function

import csv
import sys
import json
import os

theFile=sys.argv[1]
fieldnames=["title","subtitle","arg","iconfile"]

json_filename = theFile.split(".")[0]+".json"


def convert(csv_filename, json_filename, fieldnames):
	f=open(csv_filename, 'r')
	csv_reader = csv.DictReader(f,fieldnames)

	jsonf = open(json_filename,'w') 
	jsonf.write('{"items":[')

	data=""

	for r in csv_reader:
		r['uid']=r['arg']
		r['icon']={"path":r['iconfile']}
		data = data+json.dumps(r)+",\n"
	
	jsonf.write(data[:-2]) 

	jsonf.write(']}')
	f.close()
	jsonf.close()

if (not os.path.isfile(json_filename)) or (os.path.getmtime(theFile) > os.path.getmtime(json_filename)) :
	convert(theFile, json_filename, fieldnames)

with open(json_filename, 'r') as fin:
	print(fin.read(), end="")