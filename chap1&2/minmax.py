def min(x,y):
    if len(x)<len(y):
       return x
    else:
       return y
def max(x,y):
    if len(x)>len(y):
       return x
    else:
       return y
print min([1,2,3,4],[1,2])
print max([1,2,3,4],[1,2])
