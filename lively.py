""" Rajesh is very fond of numbers. With the given positive number(‘n’) ,he has to tell whether a number is lively or not. A lively number is a number which has same frequency of all integers present.

Input Description:
A integer ‘n’ will be given

Output Description:
Print 1 if number is lively and 0 if it is not lively.

Sample Input :
1212

Sample Output :
1 """

n=input()
def lively(n):
    s=''.join(list(set(n)))#removing duplicates
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if n.count(s[i])!=n.count(s[j]):
                return False
    return True
print(1 if lively(n) else 0)
