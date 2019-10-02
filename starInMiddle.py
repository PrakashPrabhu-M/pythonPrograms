'''
Given a string S, print it after changing the middle element to * 
(if the length of the string is even, change the 2 middle elements to *).
Sample Testcase :
INPUT
hello
OUTPUT
he*lo

'''

s=input()
l=len(s)//2
if len(s)%2==1:
    for i in range(len(s)):
        print(s[i] if i!=l else '*',end='')
else:
    for i in range(len(s)):
        print(s[i] if i!=l and i!=l-1 else '*',end='')
