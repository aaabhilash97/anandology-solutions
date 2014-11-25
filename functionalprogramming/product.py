def product(x,y):
	if y==0:
		return 0
	return x+product(x,y-1)
print product(4,12)
