# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 05:20:56 2019

@author: Hp
"""

'''
strings - 186
Given 2 numbers A,B. Print the GCD of a!,b!.
Input Size : B <= 10 <= A <= 1000000000
Sample Testcase :
INPUT
4 2
OUTPUT
2
'''

a,b=[int(x) for x in input().split()]

def fact(n):
    facton=1
    for i in range(1,n+1):
        facton*=i
    return facton

def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a>b:
        a%=b
        return gcd(a,b)
    elif a<b:
        b%=a
        return gcd(a,b)
    else:
        return a
print(gcd(fact(a),fact(b)))