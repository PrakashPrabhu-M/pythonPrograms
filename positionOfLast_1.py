# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 05:11:52 2019

@author: Hp
"""

'''
Print the position of first 1 from right to left, in binary representation of an Integer.
Sample Testcase :
INPUT
18
OUTPUT
2
'''

a="{:b}".format(int(input()))
print(a)
b=a[::-1]
i=b.index("1")+1
#print(len(a)-i)
print(i)