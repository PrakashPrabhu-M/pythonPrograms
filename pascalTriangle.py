n=int(input('Type a number: '))
l=[11**x for x in range(n)]
p=n
for i in range(n):
  k=l[i]
  print(' '*p,end='')
  p-=1
  for j in str(k):
    print(j,end=' ')
  print()
