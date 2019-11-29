""" Given a number N and an array of N integers, find the sum of all the negative numbers in the array.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
3 0
OUTPUT
0 """

def fun(n):
    if n<0:
        return True
    return False
input()
arr=map(int,input().split())
num=filter(fun,arr)
s=0
for i in num:
    s+=i
print(s)
