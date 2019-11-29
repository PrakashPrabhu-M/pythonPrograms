'''Given a number N, print the sum of squares of all its digits.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
12
OUTPUT
5'''

def fun(n):
    num=0
    while n:
        digit=n%10
        num+=digit*digit
        n//=10
    return num
a=int(input())
print(fun())
