""" Given a number N, check if it is a power of 2.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
64
OUTPUT
yes """
i=1
def IspowOf2(n,i):
    if n==2**i:
        return True
    elif 2**i<n:
        i+=1
        return IspowOf2(n,i)
    else:
        return False
if IspowOf2(int(input()),i):
    print('yes')
else:
    print('no')

