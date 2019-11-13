'''

You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1

Input Description:
A large number ‘n’

Output Description:
Print the max no of consecutive 1 in the number

Sample Input :
101011111

Sample Output :
5
'''

n=input()
temp=mx=0
for i in n:
  if i=='1':
    temp+=1
  else:
    mx=temp if temp>mx else mx
    temp=0
mx=temp if temp>mx else mx
print(mx if mx>0 else -1)
