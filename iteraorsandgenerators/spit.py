def split(f,n):
	fileno,i=1,0
	try:
		g=open(f.split('.')[0]+str(fileno)+'.txt','a')
		for x in open(f):
			if i==n-1:
				fileno+=1
				g=open(f.split('.')[0]+str(fileno)+'.txt','a')
				i=0
			g.write(x)
			i+=1
	except IOError:
                print "No Such File"
split("a.txt",3)			
