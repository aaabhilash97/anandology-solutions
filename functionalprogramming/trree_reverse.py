def tree_reverse(x):
	i=0
	while i<len(x):
		if isinstance(x[i],list):
			tree_reverse(x[i])
		i+=1
	x.reverse()
	return x
print tree_reverse([[1, 2], [3, [4, 5]], 6])
