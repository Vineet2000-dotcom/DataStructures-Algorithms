# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:32:25 2021

@author: Vineet
"""

a=12345
b=str(a)
list1=list(b)
i=0
j=len(list1)-1
while(i<j):
    temp=list1[i]
    list1[i]=list1[j]
    list1[j]=temp
    i+=1
    j-=1
c="".join(list1)
c=int(c)
print(c)

    
    