# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 04:41:06 2019

@author: Hp
"""

"""


You are given some words all in lower case letters your task is to print them in sorted order.

Input Description:
You are given a string ‘s’

Output Description:
Print the string in sorted order

Sample Input :
virat kohli

Sample Output :
kohli virat

"""
#sorted() can also be used
l=input().split()
l.sort()
for i in l:
	print(i,end=" ")