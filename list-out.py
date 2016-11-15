# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:31:43 2016

@author: danielle.leong
"""
# https://www.tutorialspoint.com/python/python_strings.htm

string = input("Give string  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

new = string.split(sep = ",")

for i in new:
    print(i)
 