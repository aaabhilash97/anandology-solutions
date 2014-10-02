def zip1(x,y):
   i=0
   l=min(len(x),len(y))
   p=len(y)
   o=[None]*l
   z=[(a,b) for a in x for b in y]
   k=0
   while i<l:
	o[i]=z[k]
	k=k+p+1
	i=i+1
   return o
a=[1,2,3,4,5]
b=[1,2,4,5,9,0,3]
print zip1(a,b)
