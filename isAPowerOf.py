""" Given 2 numbers N,K check if N is a power of K.
Sample Testcase :
INPUT
64 8
OUTPUT
yes """

'''
n,k=[int(x) for x in input().split()]
powers=[k**x for x in range(2,100)]
print('yes' if n in powers else 'no')
'''

i=1
n,k=[int(x) for x in input().split()]
def isPower(n,k,i):
    a=k**i
    if n==a:
        return True
    elif a<n:
        i+=1
        return isPower(n,k,i)
    else:
        return False
print('yes' if isPower(n,k,i) else 'no')
