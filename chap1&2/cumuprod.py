def cumupro(x):
    i=1
    while(i<len(x)):
         x[i]=x[i-1]*x[i]
         i=i+1
    return x
print cumupro([1,2,3,4])

