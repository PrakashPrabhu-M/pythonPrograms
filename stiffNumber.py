"""
A stiff number is a number which can only be formed by sum of two number which are co prime. You are given with a number (n).
Write a programme to determine whether a number is stiff or not

Input Description:
You are given a number n

Output Description:
Print Stiff or Not stiff

Sample Input :
9

Sample Output :
Stiff
"""

n=int(input())
def stiff(n):
    coprime=[1]#1 is a coprime number
    for i in range(100):
        for j in range(2,i//2+1):
            if i%j==0:
                coprime.append(i)
                break
    #print(coprime)
    l=[x for x in coprime if x<n]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                #print(l[i],'+',l[j],'=',n)
                return True
    return False
print('Stiff' if stiff(n) else 'Not stiff')
