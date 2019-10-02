vowels='aeiou'
S=input().lower()
flag=0
for i in S:
  if i in vowels:
    flag=1
    break
print('yes' if flag==1 else 'no')
