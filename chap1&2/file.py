import sys
def revfile(x):
    i=0
    z=len(open(x).readlines())
    rev=[None]*z
    f=open(x)
    while(i<z):
         rev[i]=f.readline()
         i=i+1
    while(i>0):
        i=i-1
        rev[i]=rev[i].strip()
        print rev[i]
        
def revline(x):
    i=0
    z=len(open(x).readlines())
    rev=[None]*z
    f=open(x)
    while(i<z):
         rev[i]=f.readline()
         rev[i]=rev[i].strip()
         print rev[i][::-1]
         i=i+1
z=sys.argv[1]
revline(z)
revfile(z)
