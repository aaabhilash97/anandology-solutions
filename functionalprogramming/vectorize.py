def square(x):
	return x*x
def vectorize(f):
	result=[]
	def g(x):
		for x1 in x:
			result.append(f(x1))
		return result
	return g
f=vectorize(square)
print f([1,2,3,4])
