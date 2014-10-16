import sys
from inspect import *
def mypydoc(x):
	p=__import__(x)
	print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
	for y in getmembers(p, predicate=lambda x: isfunction(x)):
			print y[0]
mypydoc(sys.argv[1])
