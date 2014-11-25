import os
def findfiles(x):
	for path,dirn,filen in os.walk(os.getcwd()):
		if x in filen:
			print os.path.join(path,x)

findfiles("a.txt")
