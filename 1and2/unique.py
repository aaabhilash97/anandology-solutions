def unique(x):
    i=0
    d=0
    y=[]
    while(i<len(x)):
         d=0
         for q in y:
             if(q==x[i]):
               d=1
               f=x[i] in y
         if(d!=1):
           y.append(x[i])
         i=i+1
    return y
lower=lambda x:x.lower()
upper=lambda x:x.upper()
def unique1(x,f):
    i=0
    while i<len(x):
         x[i]=f(x[i])
         i=i+1
    return unique(x)
print unique1(["py","py","qw","ui","qwqwqwqwq","ui","UI"],lower)
