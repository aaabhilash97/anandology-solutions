import itertools
def enum(x):
    return itertools.izip(range(len(list(x))),list(x))
it1=enum(['a','b','c'])
for i,c in it1:
	print i,c
