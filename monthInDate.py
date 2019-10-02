# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 05:43:31 2019

@author: Hp
"""

'''
Given a date(DD-MM-YYYY), print the month in words.
Sample Testcase :
INPUT
01-01-2018
OUTPUT
January
'''

import datetime as dt
s=input()
a=dt.datetime(1,int(s[3:5]),1)
print(a.strftime("%B"))