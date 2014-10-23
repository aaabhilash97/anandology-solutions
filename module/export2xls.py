import tablib
def xport2xls(x,y):
	data=tablib.Dataset()
	l=len(open(x).readlines())
	f=open(x)
	i=0
	while i<l:
		data.append([i,f.readline().strip()])
		i=i+1
	with open(y+'.xls','wb') as f:
		f.write(data.xls)
xport2xls(sys.argv[1],sys.argv[2])	
