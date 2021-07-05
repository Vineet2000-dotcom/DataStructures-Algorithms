# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:48:25 2021

@author: Vineet
"""

list1=[1,2,3,4,5]
i=0
j=len(list1)-1
while(i<j):
    temp=list1[i]
    list1[i]=list1[j]
    list1[j]=temp
    i+=1
    j-=1
print(*list1)
