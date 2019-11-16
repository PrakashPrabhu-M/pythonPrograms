""" 

You are given a series(In example). Go through the series in order to find the answer.
You are given with a number ‘n’. Find the nth number of series.

Input Description:
You are given a number ‘n’

Output Description:
Print the nth number of series.

Sample Input :
6

Sample Output :
21

1 3 6 10 15 21 28....
 """
n=int(input())
k=1
for i in range(2,n+1):
    k+=i
print(k)
