import os
import urllib
import sys
from string import find
def wget(x):
        r=urllib.urlopen(x)
        f=r.read()
        f=f.split('</p>')
        i=0
        while i<len(f):
                if '<p>' in f[i]:
                        c=f[i].find('<p>')
                        f[i]=f[i][c+3:]
                        i=i+1
                else:
                        del f[i]
        i=0
        while i<len(f):
                a=f[i].find('<')
                c=f[i].find('>')
                if a>0 and c>0:
                        f[i]=f[i][:a]+f[i][c+1:]
                else:
                        print f[i]
                        i=i+1
wget(sys.argv[1])

