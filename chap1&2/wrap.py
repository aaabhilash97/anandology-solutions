import sys
def wrap(x,l):
    i=0
    y=''
    s=open(x).read()
    k=len(s)
    while i<k:
	if(len(y)%l==0 and len(y)!=0):
	  y=y+'\n'
        else:
            if(s[i]!='\n'):
	     y=y+s[i]
	    else:
	     y=y+' '
	i=i+1
    return y
print wrap(sys.argv[1],int(sys.argv[2]))
