'''
Given a number N, find the nearest greater multiple of 10.
Input Size : N <= 10000
Sample Testcase :
INPUT
3
OUTPUT
10
'''
n=input()
m=10
if len(n)==1:
  print(10)
elif int(n[-1])>=5:
  print((int(n[:-1])+1)*m)
else:
  print(int(n[:-1])*m)
