# each JSON is small, there's no need in iterative processing
from __future__ import print_function
import json
import sys
import fileinput

print("Running job for category", sys.argv[1])
linenum = 0
f_tr_name = sys.argv[1]+'_train.txt'
f_te_name = sys.argv[1]+'_test.txt'

for line in fileinput.input(sys.argv[1]+'.txt'):
	linenum = linenum + 1
	try:
		# print(len(meta_review_data['categories'][0]))
		if((linenum%10 == 3) or (linenum%10 == 7)):
			f_te = open(f_te_name,'a+')
			f_te.write(line)
			f_te.close()
		else:
			f_tr = open(f_tr_name,'a+')
			f_tr.write(line)
			f_tr.close()
	except IndexError:
		continue
fileinput.close()