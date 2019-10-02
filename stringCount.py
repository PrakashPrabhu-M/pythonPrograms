# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 05:15:54 2019

@author: Hp
"""

'''
Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1
Input Size : |s| <= 100000
Sample Testcase :
INPUT
codekata a
OUTPUT
2
'''

s,k=input().split()
print(s.count(k) if s.count(k)>0 else -1)