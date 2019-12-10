def selectionSort(ar):
	for i in range(len(ar)-1,-1,-1):
		mi=i
		for j in range(i):
			if ar[mi]<ar[j]:
				mi=j
		if mi!=i:
			ar[mi],ar[i]=ar[i],ar[mi]
			print('Pass {}: {}'.format(len(ar)-1,ar))

n=[int(x) for x in input('Type a list of numbers: ').split()]
selectionSort(n)
print(n)