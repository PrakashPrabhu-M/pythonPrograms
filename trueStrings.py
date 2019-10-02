'''

 You are given a ‘true’ string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. Weight of string is the sum of ASCII value of Vowel character(s) present in the string.

Input Description:
You are given as string ‘s’ in lower cases

Output Description:
Print 1 for true and 0 for false

Sample Input :
raja

Sample Output :
0
'''

n=input()
s=0
for i in n:
  s+=ord(i)
print(1 if s%8==0 else 0)
