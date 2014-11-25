#this is a comment
import os
def pyfiles(x):
	l=[]
        for path,dirn,filen in os.walk(os.getcwd()):
                for i in filen:
			if x in i:
				l.append(os.path.join(path,i))
	print l,len(l)
pyfiles(".py")


