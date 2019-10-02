'''
Given a string S .Print the sum of weight of the String. A weight of character is defined as the ascii value of character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc

Sample Output :
294
'''
n=input()
s=0
for i in n:
  s+=ord(i)
print(s)
