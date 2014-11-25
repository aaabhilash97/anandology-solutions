def group(x,l):
    i=0
    j=0
    y=[[None]*l]*(len(x)/l)
    while(i<(len(x)/l)):
        y[i]=x[j:j+l]
	i=i+1
        j=j+l
    return y
print group([1,2,3,4,5,5,5,78,8],3)
