def reverse(x):
    i=0
    l=p=len(x)
    s=['']*l
    while i<l:
          s[i]=x[p-1]
          i=i+1
          p=p-1
    return s
print reverse(reverse([1,2,3,4]))

