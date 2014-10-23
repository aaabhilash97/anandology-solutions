import BeautifulSoup,sys
def links(x):
	soup=BeautifulSoup.BeautifulSoup("".join(open(x).read().split('\n')))
	for l in soup.findAll('a'):
		if 'lmth.' in l.get('href')[-1:-6:-1]:
			print "links==",l.get('href')
links(sys.argv[1])
	
