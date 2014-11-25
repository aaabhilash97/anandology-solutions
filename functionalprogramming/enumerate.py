def enum(x):
    ind=range(len(x))
    t=zip(ind,x)
    return [(a,b) for a,b in t]
print enum(['a','b','c'])
print [(index,value)for index, value in enum(["a", "b", "c","d"]) if index%2==0]
