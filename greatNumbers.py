'''
You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

m+j=n

 

Input Description:
You are given a number n;

Output Description:
Print Great if a number is great else print the no

Sample Input :
59

Sample Output :
Great
'''
n=int(input())
def ch(x):
  s=0
  p=1
  cp=x
  while cp:
    digit=cp%10
    s+=digit
    cp//=10
  cp=x
  while cp:
    digit=cp%10
    p*=digit
    cp//=10
  if s+p==x:
    return True
  return False
print('Great' if ch(n) else "no")
