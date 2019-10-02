# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 05:04:19 2019

@author: Hp
"""


'''


You are given two string ‘s1’ and ‘s2’. You have to tell whether these form pair of (strset) A pair of strings is said to be str set if one string is substring of other.

Input Description:
You are given two strings ‘s1’ and ‘s2’

Output Description:
Print Yes if they form strset and No if they don’t.

Sample Input :
abc ab

Sample Output :
Yes

'''
s1,s2=input().split()
if s1 in s2 or s2 in s1:
	print("Yes")
else:
	print("No")