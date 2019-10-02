# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 05:13:30 2019

@author: Hp
"""

'''
Given a string S of length N, find if it forms a double string after deleting 1 character.
Examples of double strings(meme,rara,fashionfashion).
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
abxxab
OUTPUT
NO
'''
s=input()
f=0

def double(s):
  if s[:len(s)//2]==s[len(s)//2:]:
    return True
  else:
    return False
    
for i in range(len(s)):
  if double(s[:i]+s[i+1:]):
    print("YES")
    f=1
    break
    
if f==0:
  print("NO")