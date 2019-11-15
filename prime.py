""" 
Given a number N, check whether it is prime or not.Print 'yes' if it is prime else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
no 
"""

n=int(input())
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 'no'
if eval('prime(n)')!='no':
    print('yes')
else:
    print(prime(n))
