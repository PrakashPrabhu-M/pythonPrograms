'''
Given a string S, print 2 strings such that first string containing all
characters in odd position(s) and other containing all characters in even position(s).
Sample Testcase :
INPUT
XCODE
OUTPUT
XOE CD
'''

s=input()
odd=[]
even=[]
for i in range(0,len(s),2):
    odd.append(s[i])
for i in range(1,len(s),2):
    even.append(s[i])
odd=''.join(odd)
even=''.join(even)
print(odd,even)
