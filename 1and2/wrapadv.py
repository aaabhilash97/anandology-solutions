import sys
def wrap(x,l):
    i=0
    k=0
    s=len(open(x).read().split())
    q=['']*s
    f=open(x).read().split()
    w=0
    while(i<s):
        if(len(f[i])<=(l-len(q[w]))):
          q[w]=q[w]+' '+f[i]
          i=i+1
        else:
          q[w]=q[w]+'\n'
          w=w+1
    i=1
    while(i<len(q)):
        q[0]=q[0]+q[i]
        i=i+1
    return q[0]
print wrap(sys.argv[1],int(sys.argv[2]))

