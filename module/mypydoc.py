import sys
from inspect import isfunction
def mypydoc(x):
	p=__import__(x)
	print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
	for y in dir(p):
#		if isfunction(p.y):
			print y
mypydoc(sys.argv[1])
