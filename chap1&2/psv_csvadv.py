def psv(x,y,z):
    f=open(x).readlines()
    i=0
    print f
    while i<len(f):
	  cond=z in f[i]
          if cond==False:
             f[i]=f[i].strip()
             print f[i]
             f[i]=f[i].split(y)
             i=i+1
	  else:
		f.pop(i)
          
    return f
print psv('foo.txt','!','#')                          
