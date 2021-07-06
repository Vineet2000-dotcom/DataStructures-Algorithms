# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:43:24 2021

@author: Vineet
"""

s=input()
t=input()
count=0
if len(s)!=len(t):
    print("No")
else:
    for i in s:
        if i in t:
            count+=1
            continue
        else:
            print("No")
            break
    if count==len(s):
        print("Yes")
