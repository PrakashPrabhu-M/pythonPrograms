""" Given length L and breadth B of a farm, print the area of the farm upto 5 decimal decimals.
Sample Testcase :
INPUT
1.626 2.31
OUTPUT
3.75606 """

l,b=map(float,input().split())
print('{:.5f}'.format(l*b))
