def cumusum(x):
    i=1
    while(i<len(x)):
         x[i]=x[i-1]+x[i]
         i=i+1
    return x
print cumusum([1,2,3,4])

