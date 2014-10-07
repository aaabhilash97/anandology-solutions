def valuesort(x):
	a=x.items()
	a.sort(key=lambda x:x[0])
	i=0
	ret=[]
	while i<len(a):
		ret.append(a[i][1])
		i=i+1
	return ret
print valuesort({'x': 1, 'y': 2, 'a': 3})
