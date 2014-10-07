def anagrams(x):
	from itertools import permutations
	s={}
	while len(x)>0:
		x1=x.pop()
		s[x1]=s.get(x1,[])
		s[x1].append(x1)
		print x,x1
		for z1 in x:
			perm=[''.join(p) for p in permutations(x1)]
			if z1 in perm:
				print z1
				x.remove(z1)
				s[x1].append(z1)
	return s.values()
print anagrams(['souep','eat','node','ate','done','tea'])
