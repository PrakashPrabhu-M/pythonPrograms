# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:42:58 2019

@author: Hp
"""

"""
You are given a string ‘s’. Your task is to print the characters which are not repeated.

Input Description:
You are given a string ‘s’.

Output Description:
Print the characters present once and -1 if there is no character which satisfy above condition

Sample Input :
dabbc

Sample Output :
d a c
"""

s=input()
flag=0
for i in range(len(s)):
  if s.count(s[i])==1:
    flag=1
    print(s[i],end=" ")
if flag==0:
  print(-1)