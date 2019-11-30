""" Given a number N, print its prime factors in sorted order.
Input Size : 2 <= N <= 100000
Sample Testcase :
INPUT
18
OUTPUT
2 3 """

n=int(input())

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def factors(n):
    l=[]
    for i in range(1,n+1):#range(2,n//2+1) if you don't want 1 as a factor
        if (n%i==0) and (i not in l):
            l.append(i)
    return l

nums=list(filter(prime,factors(n)))
print(*nums)
