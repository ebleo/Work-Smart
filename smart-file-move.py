"""
 _______  __   __  _______  ______    _______
|       ||  |_|  ||   _   ||    _ |  |       |
|  _____||       ||  |_|  ||   | ||  |_     _|
| |_____ |       ||       ||   |_||_   |   |
|_____  ||       ||       ||    __  |  |   |
 _____| || ||_|| ||   _   ||   |  | |  |   |
|_______||_|   |_||__| |__||___|  |_|  |___|
 __   __  _______  __   __  _______
|  |_|  ||       ||  | |  ||       |
|       ||   _   ||  |_|  ||    ___|
|       ||  | |  ||       ||   |___
|       ||  |_|  ||       ||    ___|
| ||_|| ||       | |     | |   |___
|_|   |_||_______|  |___|  |_______|

Same functionality as the previous 'move.py'--but smarter!!

# -*- coding: utf-8 -*-
Created on Wed Nov 30 13:28:26 2016

@author: danielle.leong
"""
import os

os.chdir("c:/users/danielle.leong/downloads")
flist = os.listdir("c:/users/danielle.leong/downloads")

csv_list = []

for f in flist:
    if f.endswith('.csv')
    csv_list.append(f)

name_list = []
for f in csv_list:
    s = f.split('_')
    if 'DEMO' in s:
    elif 'PANEL' in s:
    elif 'CLIENT' in s:
