import itertools
def intify(x):
	i=0
	while i<len(x):
		if isinstance(x[i],list):
			intify(x[i])
		else:
			x[i]=int(x[i])
		i+=1
	return x
def permute(x):
	s=''
	for x1 in x:
		s+=str(x1)
	return intify([list(z) for z in itertools.permutations(s)])
print permute([1,2,3])
