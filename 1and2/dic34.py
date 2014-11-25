def dec(x):
    words=open(x).read().split()
    freq={}
    for w in words:
	freq[w]=freq.get(w,0)+1
    ret=freq.items()
    ret.sort(key=lambda x:x[1])
    for z in ret:
	print z[0]
dec('foo.txt')
