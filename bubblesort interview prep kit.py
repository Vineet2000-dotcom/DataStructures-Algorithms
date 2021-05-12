# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:28:23 2021

@author: Vineet
"""


n=int(input())
list1=list(map(int,input().split()[:n]))
count=0
for i in range(n-1):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            count+=1
c=list1[0]
d=list1[-1]
print('Array is sorted in', count, 'swaps.')
print('First Element:', list1[0])
print('Last Element:', list1[-1])