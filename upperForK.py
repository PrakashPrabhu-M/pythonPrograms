# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 05:10:26 2019

@author: Hp
"""

'''
Given a string and a number K, change every kth character to uppercase from beginning in string.

i/p:
    string 2
o/p:
    sTrInG
'''
s,n=input().split()
s=" "+s
for i in range(1,len(s)):
	print(s[i].upper() if (i%int(n)==0 if int(n)!=0 else i) else s[i],end="")