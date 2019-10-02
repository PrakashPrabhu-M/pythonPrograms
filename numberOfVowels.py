'''
211.strings
Given a number N and an array of N strings, sort the strings based on the number of vowels in each of the strings in descending order.
Input Size : N <= 1000
Sample Testcase :
INPUT
3
Vishal
Aaae
Awqr
OUTPUT
Aaae
Vishal
Awqr
'''

n=int(input())
l=[]
d={}

for _ in range(n):
    l.append(input())

for i in l:
    d[i]=i.count("a")+i.count("e")+i.count("i")+i.count("o")+i.count("u")+i.count("A")+i.count("E")+i.count("I")+i.count("O")+i.count("U")

for i in sorted(d,key=lambda x: x[1],reverse=False):
    print(i)