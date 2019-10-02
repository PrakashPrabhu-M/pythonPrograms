# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:54:36 2019

@author: Hp
"""

"""
Joyal was given a sentence. Joyal is given a task,The task is to delete the two words that comes together and print the remaining sentence which is left.

Input Description:
You are given a sentence ‘s’

Output Description:
Print the all the words that are left.Print-1 if no words are left

Sample Input :
I am john cena cena john

Sample Output :
I am
"""

n=input().split()
flag=0
while flag==0:
    flag=1
    for i in range(len(n)-1):
      #print(i)
      if n[i]==n[i+1]:
        n.remove(n[i])
        n.remove(n[i])
        flag=0
        break
s=" ".join(n)
print(s if s!="" else -1)
