import sys
def filesprint(filenames):
	for files in filenames:
	   try:
		for line in open(files):
			if len(line)>40:
				print line
	   except IOError:
		print "no fiiles"
l=[sys.argv[x] for x in range(1,len(sys.argv))]
filesprint(l)
