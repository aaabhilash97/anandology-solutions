def psv(x):
    f=open(x).read().split()
    i=0
    while i<len(f):
          f[i]=f[i].split(',')
          i=i+1
    return f
print psv('foo.txt')
