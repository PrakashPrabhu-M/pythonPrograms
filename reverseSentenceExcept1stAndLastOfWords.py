# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 06:01:15 2019

@author: Hp
"""
'''
string-64
Given a string S consisting of a sentence, the task is to reverse every word of the sentence except the first and last character of the words.
Sample Testcase :
INPUT
guvi coding platform
OUTPUT
gvui cnidog proftalm.
'''
s=input().split()
for i in s:
  print(i[0],i[len(i)-2:0:-1],i[-1],sep="",end=" ")