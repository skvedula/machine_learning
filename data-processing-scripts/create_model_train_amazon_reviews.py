# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:52:34 2016

@author: skvedula
"""
from __future__ import print_function
import sys
import json
from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

wordcount={}
linenumber=0
flag = 0
with open(sys.argv[1], "r") as ins:
    for line in ins:
        linenumber = linenumber+1
        data = json.loads(line)
        if data["description"]:
            flag = 1
            description = data["description"]
            description = description.replace("."," ")        
            for dword in description.split():
                cleaned_dWord = strip_punctuation(dword)
                cleaned_dWord = cleaned_dWord.lower()
                if cleaned_dWord not in wordcount:
                    wordcount[cleaned_dWord] = 1
                else:
                    wordcount[cleaned_dWord] += 1                
        # if data["descriptions"]:
        #     description = data["descriptions"]
        #     for dword in description.split():
        #         cleaned_dWord = strip_punctuation(dword)
        #         cleaned_dWord = cleaned_dWord.lower()
        #         if cleaned_dWord not in wordcount:
        #             wordcount[cleaned_dWord] = 1
        #         else:
        #             wordcount[cleaned_dWord] += 1
if flag:
    with open('dcount_'+sys.argv[1], 'w+') as output:
        for k,v in wordcount.items():
            print(k, "\t",v, "\t",linenumber, file=output)