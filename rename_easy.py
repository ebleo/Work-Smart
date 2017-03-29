# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:51:54 2017

@author: danielle.leong
"""

import os

mypath = r'C:\Users\danielle.leong\Downloads\00'

os.chdir(mypath)

myfiles = os.listdir(mypath)

renames = ['C3.csv', 'LIVE.csv', 'PANEL C3.csv', 'PANEL LIVE.csv', \
           'C3 DEMO 1.csv', 'C3 DEMO 2.csv', 'C3 DEMO 3.csv', 'C3 DEMO 4.csv', \
           'C7 DEMO 1.csv', 'C7 DEMO 2.csv', 'C7 DEMO 3.csv', 'C7 DEMO 4.csv',\
           'LIVE DEMO 1.csv', 'LIVE DEMO 2.csv', 'LIVE DEMO 3.csv', 'LIVE DEMO 4.csv']

if len(renames) == len(myfiles):
    print('qty match')
    pairs = zip(myfiles, renames)
    for old, new in pairs:
        os.rename(old, new)
else:
    print('no match')
    clientbool = input('client only files? INPUT 1 or 0    ')
    
if clientbool:
    names = renames[:2] + renames[4:]
    pairs = zip(myfiles, names)
    for old, new in pairs:
        os.rename(old, new)