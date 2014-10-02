def map1(f,x):
    return [f(x) for a in x]
def square(x):
    return x*x
def cube(x):
    return x**3
print map(square,[1,2,3])
