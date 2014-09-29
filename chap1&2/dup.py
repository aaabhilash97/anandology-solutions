def dup(x):
    i=0
    y=[]*len(x)
    while(i<len(x)):
         d=0
         while(d<len(x)):
              if(i!=d):
                if(x[i]==x[d]):
                  y.append(x[i])
                  z=x[i]
                  for q in x:
                     if(q==z):
                        x[i]=None
              d=d+1
         i=i+1
    return y
print dup([1,2,3,4,2])
