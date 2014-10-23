import sys
def mypydoc(x):
	p=__import__(x)
	print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
	for y in dir(p):
		print y
mypydoc(sys.argv[1])
