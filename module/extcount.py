import sys
import os
def extcount(x):
	ls=os.listdir(x)
	i=0
	d={}
	while i<len(ls):
		ls[i]=ls[i].split('.')
		if(len(ls[i])>1):
			d[ls[i][1]]=d.get(ls[i][1],0)+1
		i=i+1
	for keys,values in d.items():
		print keys,values
extcount(sys.argv[1])
