def invertdict(x):
	dic={}
	tup=x.items()
	i=0
	while i<len(tup):
		dic[tup[i][1]]=tup[i][0]
		i=i+1
	return dic
print invertdict({'x': 1, 'y': 2, 'z': 3})
