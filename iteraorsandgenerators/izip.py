def enum(x,y):
    return iter(zip(x,y))
p=enum([1,2,2],[224,434,3,2])
print p.next()
