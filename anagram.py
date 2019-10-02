# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:23:16 2019

@author: Hp
"""

"""
Given a number N and an array of N strings, find the number of strings that are an anagram of 'kabali'.
Input Size : 1 <= N <= 1000
Sample Testcase :
INPUT
5
kabali
kaabli
kababa
kab
kabail
OUTPUT
3
"""

n=int(input())
s=[]
for i in range(n):
    s.append(input())
count=0
for i in range(n):
    flag=0
    for x in "kabali":
        if x in s[i]:
            flag+=1
    if flag==6:
        count+=1
print(count)