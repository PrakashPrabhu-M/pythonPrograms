""" Given two numbers N,K followed by an array of N elements, print the array after doing right shift K times (in cyclic manner).
Input Size : 1 <= N, K <= 100000
Sample Testcase :
INPUT
3 2
7 2 3
OUTPUT
2 3 7 """

n,k=map(int,input().split())
arr=list(map(int,input().split()))
def rightShift(arr,num):
    arr=arr[-(num%n):]+arr[:-(num%n)]
    return arr 
print(*rightShift(arr,k))
