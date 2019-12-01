""" 

Rahul was learning about numbers in list. He came across one word ground of a number.

A ground of a number is defined as the number which is just smaller or equal to the number given to you.Hence he started solving some assignments related to it. He got struck in some questions. Your task is to help him.

 

O(n) time complexity

O(n) Auxilary space

Input Description:
First line contains two numbers ‘n’ denoting number of integers and ‘k’ whose ground is to be check. Next line contains n space separated numbers.

Output Description:
Print the index of val.Print -1 if equal or near exqual number

Sample Input :
7 3
1 2 3 4 5 6 7

Sample Output :
2
"""

a,b=[int(x) for x in input().split()]
ar=[int(x) for x in input().split()]
flag=0
for i in ar:
    for j in range(b,-1,-1):
        if j in ar:
            flag=1
            print(ar.index(j))
            break
    print(-1 if flag==0 else '')
    break
      
