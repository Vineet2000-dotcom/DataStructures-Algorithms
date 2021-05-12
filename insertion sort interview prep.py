# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:49:29 2021

@author: Vineet
"""


def insertionsort(prices,n):
    for i in range(1,len(prices)):
        e=prices[i]
        j=i-1
        while(j>=0 and prices[j]>e):
            prices[j+1]=prices[j]
            j=j-1
        prices[j+1]=e
        
    
    
n,k=map(int,input().split())
prices=list(map(int,input().split()[:n]))
insertionsort(prices,n)

sum=0
count=0
for i in prices:
    if sum+i<=k:
        sum=sum+i
        count+=1
    
        
print(count)
          
        