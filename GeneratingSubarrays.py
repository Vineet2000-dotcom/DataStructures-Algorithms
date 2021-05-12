# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:28:02 2021

@author: Vineet
"""


n=int(input())
list1=list(map(int,input().split()))
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        for k in range(i,j+1):
            print(list1[k],end=" ")
        print ("\n",end="")
