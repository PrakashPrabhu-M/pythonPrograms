# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:20:14 2019

@author: Hp
"""
'''
Given a number N and an array of N integers, print the suffix sum array.
Input Size : N <= 100000
Sample Testcase :
INPUT
4
2 4 4 2
OUTPUT
12 10 6 2
'''
n=int(input())
l=[int(x) for x in input().split()]

for j in range(-1,n-1):
    s=0
    for i in range(n-1,j,-1):
        s+=l[i]
    print(s,end=" ")