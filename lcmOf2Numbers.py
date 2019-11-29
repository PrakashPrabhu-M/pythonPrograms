""" Given two numbers L,R print the smallest number which is divisible by both L and R.
Input Size : 1 <= L,R <= 100000
Sample Testcase :
INPUT
10 130
OUTPUT
130 """

#lcm(a,b)=(a*b)/gcd(a,b) this is used here

a,b=list(map(int,input().split()))
import math
lcm=(a*b)//math.gcd(a,b)
print(lcm)
