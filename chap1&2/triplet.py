import sys
def triplet(n):
    return [(a,b,c) for a in range(n) for b in range(n) for c in range(n) if a+b==c and a!=0 and b!=0 and c!=0]
print triplet(int(sys.argv[1]))
