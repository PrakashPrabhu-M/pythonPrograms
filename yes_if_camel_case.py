# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:45:45 2019

@author: Hp
"""

"""
Given a sentence S as input check whether it is in camelcase.
input size : |s| <= 100000
Sample Testcase :
INPUT
Good Laptop
OUTPUT
yes
"""

s=input().split()
flag=0
for i in range(len(s)):
  if s[i][0]==s[i][0].lower():
    flag=1
print("no" if flag==1 else "yes")