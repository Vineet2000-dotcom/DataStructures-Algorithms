# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:23:20 2021

@author: Vineet
"""
#Given a sorted array find pair of elements that sum to k

flag = 0
A = []
n = int(input("enter number of elements "))
print("enter the array ")
for i in range(0, n):
    ele = int(input())
    A.append(ele)
print(A)
k = int(input("enter the sum: "))
for i in range(0, n):
    for j in range(i + 1, n):
        if A[i] + A[j] == k:
            print(A[i], ",", A[j], "\n")
            flag = 1
if flag == 0:
    print("No pairs found")