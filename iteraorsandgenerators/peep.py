def peep(x):
	return x.next(),iter(list(x))
it = iter(range(5))
y, it1 = peep(it)
print y, list(it1)
