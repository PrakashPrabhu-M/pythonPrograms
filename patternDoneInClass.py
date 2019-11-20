n=10
l=[x for x in (' '*n)]
for i in range(1,n):
  l[i]=str(1)
  for j in range(2,i+1):
    l[i]+=str(j)
  if i!=1:
    l[i]+='1'

for i in l:
  print(i.center(n))
for i in l[::-1]:
  print(i.center(n))

