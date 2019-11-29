""" Given a number 'N' print the sum of each digit to the power of number of digits in given input.
Example :
Input => 1234
=> ( 1 ^ 4 ) + ( 2 ^ 4 ) + ( 3 ^ 4 ) + ( 4 ^ 4 )
=> 1 + 16 + 81 + 256
Output => 354
N <=100000000000
Sample Testcase :
INPUT
1234
OUTPUT
354 """

n=int(input())

def fun(n):
    power=0
    cp=n
    sums=0
    while cp:
        power+=1
        cp//=10
    while n:
        digit=n%10
        sums+=digit**power
        n//=10
    return sums

print(fun(n))    
