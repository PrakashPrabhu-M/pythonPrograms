'''
Write a program to get a string S,
Type of conversion (1 - Convert to Lowercase, 2 - Convert to Uppercase) T, and integer P .
Convert the case of the letters in the positions which are multiples of P.(1 based indexing).

Input Description:
Given a string S, Type of conversion T, and integer P

Output Description:
Convert the case of the letters and print the string

Sample Input :
ProFiLe
1
2

Sample Output :
Profile
'''
s=[x for x in ' '+input()]
t=int(input())
p=int(input())
if t==1:
    for i in range(0,len(s),p):
        s[i]=s[i].lower()
    s=''.join(s)
else:
    for i in range(0,len(s),p):
        s[i]=s[i].upper()
    s=''.join(s)
print(s.strip())

