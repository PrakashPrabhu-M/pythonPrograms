""" 

harish learnt about gcd and and want to apply the concept to find the gcd of n numbers.

But in between he got stuck and now he is asking for some help your task is to print the gcd of n numbers and print -1 if there is no gcd possible

 

Input Description:
You are given an array size ‘n’.Next line contains n space separated numbers.

Output Description:
Your task is to print the gcd of number

Sample Input :
6
2 4 8 16

Sample Output :
2
 """

from math import gcd
arr=list(map(int,input().split()))
d=gcd(arr[0],arr[1])
for i in range(2,len(arr)):
    d=gcd(d,arr[i])
print(d)
