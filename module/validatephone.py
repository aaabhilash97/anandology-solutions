import string
def vallidate(x):
	i=0
	while i<len(x):
		if x[i] in string.digits:
			con=True;
		else:
			con=False
			break
		i=i+1
	if con==True and (len(x)>8 and len(x)<13):
		print "its a valid phone nu"
	else:
		print "not valid"
vallidate("9895774319")
