# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:10:42 2017

@author: danielle.leong
"""

import os

mypath = r'C:\Users\danielle.leong\Downloads\00'

os.chdir(mypath)

myfiles = os.listdir(mypath)

fmove = ['C3.csv', 'LIVE.csv', \
           'C3 DEMO 1.csv', 'C3 DEMO 2.csv', 'C3 DEMO 3.csv', 'C3 DEMO 4.csv', \
           'C7 DEMO 1.csv', 'C7 DEMO 2.csv', 'C7 DEMO 3.csv', 'C7 DEMO 4.csv',\
           'LIVE DEMO 1.csv', 'LIVE DEMO 2.csv', 'LIVE DEMO 3.csv', 'LIVE DEMO 4.csv']

for file in myfiles:
    if file in fmove:
        if file in fmove[:2]:
            newloc = r'C:\Users\danielle.leong\Desktop\Kantar Pull\Client\\'
            newloc = newloc + file
            oldloc = mypath + '\\' + file
            os.rename(oldloc, newloc)
        elif file in fmove[2:]:
            newloc = r'C:\Users\danielle.leong\Desktop\Kantar Pull\Pool Runs\\'
            newloc = newloc + file
            oldloc = mypath + '\\' + file
            os.rename(oldloc, newloc)