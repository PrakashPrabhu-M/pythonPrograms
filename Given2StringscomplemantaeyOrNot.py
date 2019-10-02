# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 05:52:15 2019

@author: Hp
"""

'''
Write a program which displays whether the given two strings are complementary or not. Assume both the string contains unique capital alphabets in alphabetical order. Their total length has to be 26. If we join alphabets of both the strings we should get all capital letters exactly once, then only we can call them as complementary. Print complementary/non-complementary.
Sample Testcase :
INPUT
ABDCFGIJKLMNOPQUVWXYZ
EHRST
OUTPUT
complementary
'''

s1,s2=input().split()
s3=s1+s2
def if_repeat_in(a):
  for i in a:
    if a.count(i)>2:
      return True
  return False
if len(s3)==26 and not(if_repeat_in(s3)):
  print("complementary")
else:
  print("non-complementary")