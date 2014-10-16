from zipfile import *
import sys
def zip(x,y):
	f=ZipFile(x,'w')
	for n in y:
		f.write(n)
zip(sys.argv[1],sys.argv[2:])
