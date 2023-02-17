# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:11:43 2022

@author: Vaibhav Tiwari
"""

import json 
f='name.json'
try:
    q=open(f,'r')
    q1=json.load(q)
    print(q1)
except:
    n=input("Enter your name : ")
    q=open(f,'w')
    json.dump(n,q)
    print("We will remember you")
else:
    print("Welcome back user")
    
#########################################################

import json
def h1():
    try:
        a=open(f,'r')
        q=json.load(a)
    except:
        return None
    else:
        return q

def h2():
    u=h1()
    if u:
        print("Welcome back user")
    else:
        u=input("Enter your name : ")
        a=open(f,'w')
        json.dump(u,a)
f='name.json'
h2()    

#######################################################

import json
def h1():
    try:
        a=open(f,'r')
        q=json.load(a)
        print(q)
    except:
        return None
    else:
        return q

def h2():
    
    u=input("Enter your name : ")
    a=open(f,'w')
    json.dump(u,a)
        
def h3():
    u=h1()
    if u:
        print("Welcome back user")
    else:
        h2()
        print("We will save your data")
f='name.json'
h3()
