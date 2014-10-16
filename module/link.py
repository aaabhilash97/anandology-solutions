from string import find
from urllib import urlopen
def links(x):
	n=1
	s=[]
	f=urlopen(x).read()
	while n>0:
		n=f.find('"http://')
		f=f[n+1:]
		n=f.find('"')
		s.append(f[:n])
		f=f[n:]
		n=f.find('"http://')
	print s
import sys
links(sys.argv[1])
