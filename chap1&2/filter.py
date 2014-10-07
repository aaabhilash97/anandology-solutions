def filter(f,x):
    return [a for a in x if f(a)==True]
def even(x): return x %2 == 0
print filter(even,range(10))
