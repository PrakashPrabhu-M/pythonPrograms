'''
Given a number N and an array of N integers, find the Bitwise AND of the array.
Input Size N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
0
'''
N=input()
a=map(int,input().split())
res=1
for i in a:
	res&=i
print(res)