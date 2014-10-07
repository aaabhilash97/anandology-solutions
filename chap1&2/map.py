def square(x):
    return x*x
def cube(x):
    return x**3
def map1(f,x):
    return [f(a) for a in x]
print map1(chr,range(97,123))
