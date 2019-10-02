# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 04:50:48 2019

@author: Hp
"""

'''
Given 2 strings S,X. Print yes if their lengths are co-prime otherwise no.
Input Size : 1 <= |s|, |x| <= 100000
Sample Testcase :
INPUT
GUVI GREAT
OUTPUT
yes
'''

s1,s2=input().split()
[n1,n2]=[len(s1),len(s2)]

def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a>b:
        a=a%b
        return gcd(a,b)
    elif b>a:
        b=b%a
        return gcd(a,b)

#print(gcd(n1,n2))
print("yes" if gcd(n1,n2)==1 else "no")