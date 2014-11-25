import os
def numlines(x):
        l=0
        for path,y,z in os.walk(os.getcwd()):
                for i in z:
                        if x in i:
				il=0
				for f in open(i):
					if f[0] not in ['#','\n']:
						print f[0],1
						l+=1
						il+=1
				print os.path.join(path,i),":-",il
        print "Total:- ",l
numlines(".py")
