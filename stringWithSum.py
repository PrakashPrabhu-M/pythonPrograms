# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 05:26:58 2019

@author: Hp
"""

'''


You are given a string ‘s’.Your task is to print the string in the order they are present and then sum of digits.

Input Description:
You are given a string ‘s’.

Output Description:
Print the string and then at last sum of all the digits

Sample Input :
AC30BD40

Sample Output :
ACBD7

'''
s=0
for i in input():
    if 64<ord(i)<122:
        print(i,end="")
    else:
        s+=int(i)
print(s)