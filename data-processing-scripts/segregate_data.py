# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 12:52:34 2016

@author: skvedula
"""
# each JSON is small, there's no need in iterative processing
from __future__ import print_function
import json
import sys
import fileinput

bag_Of_subCats = {}

category = sys.argv[1]
category = category.split("_")
del category[:2]
category = "_".join(category)
print("Running job for category", category)
for line in fileinput.input([sys.argv[1]+'.json']):
	meta_review_data = json.loads(line)
	if(len(meta_review_data['categories']) > 0):
		for i, category in enumerate(meta_review_data['categories']):
			try:
				if(len(meta_review_data['categories'][i]) > 1):
					l1_cat = (meta_review_data['categories'][i][0]).split(" ")
					l1_cat = "_".join(l1_cat)
					l2_cat = (meta_review_data['categories'][i][1]).split(" ")
					l2_cat = "_".join(l2_cat)
					filename = str(l1_cat)+"###"+str(l2_cat)
					f_name = filename + '.txt'
					f = open(f_name,'a+')
					f.write(line)
					f.close()					
					if(bag_Of_subCats.get(filename)):
						bag_Of_subCats[filename] += 1
					else:
						bag_Of_subCats[filename] = 1
				else:
					l1_cat = (meta_review_data['categories'][i][0]).split(" ")
					l1_cat = "_".join(l1_cat)
					filename = str(l1_cat)
					f_name = filename + '.txt'
					f = open(f_name,'a+')
					f.write(line)
					f.close()					
					if(bag_Of_subCats.get(filename)):
						bag_Of_subCats[filename] += 1
					else:
						bag_Of_subCats[filename] = 1
			except IndexError:
				continue