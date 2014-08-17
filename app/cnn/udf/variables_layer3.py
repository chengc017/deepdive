#! /usr/bin/env python
#Author: Amir S 

from helper.easierlife import *
import json
import fileinput

BlockSize=5
FID_IN=4
FID_OUT=6
for row in fileinput.input():
	obj = json.loads(row)
	image_id = obj["image_id"]
	ws = obj ["ws"]
	ls = obj ["ls"]
	n_row=ws[0]
	n_col=ls[0]
	values=[]
	for i in range(0,n_row-BlockSize+1):
		for j in range(0,n_col-BlockSize+1):
			values.append(None)		
	for f in range(0,FID_OUT):
		print json.dumps({
			"image_id":image_id,
			"fid":f,
			"num_rows":n_row-BlockSize+1,
			"num_cols":n_col-BlockSize+1,
			"values":values
			})


				
					