# -*- coding: utf-8 -*-
######
"""
######
Created on Wed Sep 21 12:52:34 2016
######
######
@author: skvedula
######
"""
######
# each JSON is small, there's no need in iterative processing
######
from __future__ import print_function
######
import json
######
import sys
######
import fileinput
######
######
err_case = 0
######
bagOfProducts = {}
######
with open(sys.argv[1]+'.json', 'r') as f:
######
  for num, line in enumerate(f, 1):
######
		try:
######
			data = json.loads(line)
######
			# building dictionary
######
			bagOfProducts[data['asin']] = {"categories": data['categories'], "description": data.get('description')}
######
			# print(num)
######
		except ValueError:
######
			err_case = err_case + 1
######
			continue
######
f.close()
######
print(err_case)
######
# bagOfProducts contains productid-key with respective descriptions and categories
######
with open(sys.argv[3]+'.json', 'w+') as output:
######
	for line in fileinput.input([sys.argv[2]+'.json']):
######
		review_data = json.loads(line)
######
		if bagOfProducts.get(review_data['asin']):
######
			# Here we got the dictionary of id <--> Description; Category
######
			for k,v in (bagOfProducts[review_data['asin']]).iteritems():
######
				review_data[k] = v
######
			# write the merged data into a new file
######
			print(json.dumps(review_data), file=output)
######
	fileinput.close()######