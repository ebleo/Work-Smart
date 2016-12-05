"""
# -*- coding: utf-8 -*-
Created on Wed Nov 30 13:28:26 2016

@author: danielle.leong
"""
#%%
'''
STATUS: functional cell

test file located at:
'c:/users/danielle.leong/documents'
filename:
'test.txt'
'''
# file operations
import os
os.chdir('c:/users/danielle.leong/documents')
f = open('test.txt')
text_list = f.readlines()


#%%
'''
STATUS: functional cell

dictionary properly stores valeus
'''
# to remove line endings, "\n"
newt = []

for s in text:
    if '\n' in s:
        x = s.find('\n')
        new = s[:x] + s[(x + 1):]
        newt.append(new)

# creating dicitonary
d = {}
for line in newt:
    l = line.split(' ')
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
#%%
# POC
d = {}
d['pants'] = 5
print(d['pants'] )
d['pants'] += 10
