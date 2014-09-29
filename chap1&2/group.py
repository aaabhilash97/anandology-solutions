def group(x,l):
    i=0
    j=0
    p=0
    y=[[None]*l]*(len(x)/l)
    ys=[None]*l
    z=len(x)/l
    while(j<z):
          while(i<l):
	       print j,i,p
               ys.appenx.pop()
           #    y[j][i]=x[p]
               i=i+1
               p=p+1
          y[j]=ys
          i=0
          j=j+1
    return y
print group([1,3,2,2,2,9,7,2,4],3)
         
