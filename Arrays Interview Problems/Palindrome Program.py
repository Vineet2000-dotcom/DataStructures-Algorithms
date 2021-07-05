# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:04:45 2021

@author: Vineet
"""
##first appproach
s="malayalam"
a=s[::-1]
if a==s:
    print("Yes")
else:
    print("No")
    
##  second approach
s="nitin"
list1=list(s)
def reverse_string(list1):
    i=0
    j=len(list1)-1
    for i in range(0,len(list1)):
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp
        i+=1
        j-=1
    return list1
s1=reverse_string(list1)
s2="".join(s1)
if s==s2:
    print("Yes")
else:
    print("No")


