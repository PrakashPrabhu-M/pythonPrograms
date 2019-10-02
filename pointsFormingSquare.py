# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:57:48 2019

@author: Hp
"""

"""
Check whether the given 4 points form a square or not.
Example:
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes
"""

ax,ay=[int(x) for x in input().split()]
bx,by=[int(x) for x in input().split()]
cx,cy=[int(x) for x in input().split()]
dx,dy=[int(x) for x in input().split()]

AB=((ax-bx)**2+(ay-by)**2)**(1/2)
AC=((ax-cx)**2+(ay-cy)**2)**(1/2)
AD=((ax-dx)**2+(ay-dy)**2)**(1/2)

if (AB==AC and AD==((bx-cx)**2+(by-cy)**2)**(1/2)) or (AB==AD and AC==((bx-dx)**2+(by-dy)**2)**(1/2)):
  print("yes")
else:
  print("no")
  