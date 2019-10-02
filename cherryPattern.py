# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:22:15 2019

@author: Hp
"""

'''
Chan’s girlfriend's birthday is near, so he wants to surprise her by making a special cake for her. Chan knows that his girlfriend likes cherries on the cake, so he puts cherries on the top of the cake, but he was not satisfied. Therefore, he decided to replace some of the cherries to make a beautiful pattern. However, Chan has a lot of other work to do so he decided to ask for your help. The cherries are of two colors red and green. Now Chan wants the cherries to be placed in such a way that each cherry of one color must be adjacent to only cherries of the other color, two cherries are adjacent if they share a side. Now Chan has asked for your help in making that pattern on the cake.You can replace any cherry of given color with the other color. But there is a cost for each replacement: if you replace a red cherry with a green one, the cost is 5 units and if you replace a green cherry with a red one, the cost is 3 units. Help your friend Chan by making the cake special with minimum cost.
Input Size : N<=1000, M<=1000
Example:
INPUT
2 3
RRG
GGR
OUTPUT
8

100 Geek coins
'''

n=[int(x) for x in input().split()]
s=[]
c=0

for i in range(n[0]):#n[0] is number of inputs
  s.append(input()+" ")

for i in s:
  for j in range(n[1]):#n[1] is length of each inputs
    if i[j]==i[j+1]:
      if i[j]=="R":
        c+=5
      elif i[j]=="G":
        c+=3

print(c)
    