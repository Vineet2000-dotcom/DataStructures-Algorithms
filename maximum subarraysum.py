# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:18:14 2021

@author: Vineet
"""


n=int(input())

list1=list(map(int,input().split()))
maximumsum=0
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        currentsum=0

        for k in range(i,j+1):
           currentsum=currentsum + list1[k]
        if currentsum>maximumsum:
            maximumsum=currentsum
print(maximumsum)
    