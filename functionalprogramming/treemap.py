def treemap(f,l):
	i=0
	while i<len(l):
		if isinstance(l[i],list):
			treemap(f,l[i])
		else:
			l[i]=f(l[i])
		i+=1
	return l
l=[1, 2, [3, 4, [5]]]
print treemap(lambda x: x*x, l)
