def unique(x):
    i=0
    y=[]*len(x)
    x.sort(key=lambda x:x.lower)
    print x
    while(i<len(x)):
         d=0
         while(d<len(x)):
              if(i!=d):
                if(x[i].lower()==x[d].lower()):
                  y.append(x[i])
                  z=x[i]
                  for q in x:
                     if(q.lower()==z.lower()):
                        x[i]=''
              d=d+1
         i=i+1
    return y
print unique(["python", "java", "Python", "Java","A","a","abhilash","ABHILASH"])
