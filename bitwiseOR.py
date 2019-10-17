'''
Given a number N and an array of N integers, find the Bitwise OR of the array.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
'''
N=int(input())
a=map(int,input().split())
res=0
for i in a:
	res|=i
print(res)