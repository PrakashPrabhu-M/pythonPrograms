# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 05:20:04 2019

@author: Hp
"""

'''
Given an arraylist A of string type which has name#mark1#mark2#mark3 format. Retrieve the name of the student who has scored max marks(total of three).
for eg: input: {'arun#12#12#12','deepak#13#12#12'}
output: Deepak
Input Size : A <= 100000
Sample Testcase :
INPUT
arun#12#12#12
deepak#13#12#12
OUTPUT
deepak
'''

a=input().split("#")
b=input().split("#")
n1=a[1]+a[2]+a[3]
n2=b[1]+b[2]+b[3]
print(a[0] if n1>n2 else b[0])