# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:40:00 2022

@author: Vaibhav Tiwari
"""

import json
s=[1,2,3,4,5,6]
s1='s.json'
a=open(s1,'w')

json.dump(s,a)

#######################################

import json 
s=input("Enter your name : ")
a=open('s.json','w')
json.dump(s,a)
