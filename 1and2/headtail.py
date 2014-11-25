def ht(x,p):
    i=0
    l=len(open(x).readlines())-1
    k=l-p
    f=open(x).readlines()
    print "\nfirst %d line\n------------------"%(p)
    while i<10:
	f[i]=f[i].strip('\n')
	print f[i]
	i=i+1
    print "\nlast %d lines\n------------------"%(p)
    while l>k:
	f[l]=f[l].strip('\n')
        print f[l]
	l=l-1
    
import sys
ht(sys.argv[1],int(sys.argv[2]))
