def bubbleSort(ar):
	for i in range(len(ar)-1,-1,-1):
		for j in range(i):
			if ar[j]>ar[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
		print('Pass {}: {}'.format(len(ar)-i,ar))
		
a=[int(x) for x in input('Type a list of numbers: ').split()]
bubbleSort(a)
print(a)