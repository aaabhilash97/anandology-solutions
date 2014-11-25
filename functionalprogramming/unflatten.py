def unflatten_dict(a, result=None):
    if result is None:
        result = {}
    new={}
    for x in a:
        y=a[x]
        if '.' in x:
	    l=x.split('.')
	    i=0
	    while i<len(l):
		new[l[i+1]]=y
		result[l[i]]=new
		i+=2
        else:
           result[x]=y
    return result
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
