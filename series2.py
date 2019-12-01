""" you are given with ‘arasu’ series(shown in example).You have to understand it and you will be given a number ‘n’ ,you have to print the series till n numbers.

Input Description:
You are given a number n;

Output Description:
Print series till nth number

Sample Input :
4

Sample Output :
2 5 10 17
 """

def series(N,l,n=3,a=2):
    l.append(a)
    if N==1:
        return l
    else:
        a+=n
        n+=2
        return series(N-1,l,n,a)
  
l=series(int(input()),[])
print(*l)
