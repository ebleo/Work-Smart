# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:31:43 2016

@author: danielle.leong
"""
# https://www.tutorialspoint.com/python/python_strings.htm
#%%
string = input("Give string  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

new = string.split(sep = ",")

for i in range(len(new)):
    print(new[i])
 
    
    
#%% to remove spaces
for i in range(len(new)):
    newer = new[i]    
#    print(newer)
    new[i] = newer.replace(' ','')    
    print(new[i])
