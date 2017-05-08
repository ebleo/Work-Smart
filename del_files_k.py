# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:07:18 2017

@author: danielle.leong
"""

import os

del_true = []
folds = ['00', 'Kantar Client', 'Kantar Pool']

dl_path = r'C:\Users\danielle.leong\Downloads\00'
k_paths = [r'C:\Users\danielle.leong\Desktop\Kantar Pull\Client', \
           r'C:\Users\danielle.leong\Desktop\Kantar Pull\Pool Runs']

dl_00 = os.listdir(dl_path)
kp1 = os.listdir(k_paths[0])
kp2 = os.listdir(k_paths[1])

while len(del_true) < 3:
    qstr = "delete folder " + folds[len(del_true)] + "?  "
    delTF = input(qstr)
    del_true.append(delTF)

if del_true[0]:
    for file in dl_00:
        full_file = dl_path + "\\" + file
        os.remove(full_file)
        
if del_true[0]:
    for file in kp1:
        full_file = k_paths[0] + "\\" + file
        os.remove(full_file)
        
if del_true[0]:
    for file in kp2:
        full_file = k_paths[1] + "\\" + file
        os.remove(full_file)        