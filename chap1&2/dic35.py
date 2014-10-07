def dec(x):
    p=['print','def','items()','import']
    c=['printf("','#include','<stdio.h>','#include<stdlib.h>','scanf("','getchar();','EOF',]
    deter={'python':0,'c':0}
    words=open(x).read().split()
    freq={}
    for w in words:
        freq[w]=freq.get(w,0)+1
    ret=freq.items()
    ret.sort(key=lambda x:x[1])
    for z in ret:
	cond4p=z[0] in p
	cond4c=z[0] in c
        if(cond4p==True):
	   deter['python']=deter.get('python',0)+1;
        elif(cond4c==True):
	   deter['c']=deter.get('c',0)+1;
    if(deter['c']==0):
	print "it is a python prog"
    elif(deter['python']==0):
	print "it is a cprog"
    else:
	print "it is a text"
dec('foo.txt') 
