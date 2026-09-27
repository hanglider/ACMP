from fnmatch import *
a, b = open(0).read().split()
print(["NO", "YES"][fnmatch(a, b) or fnmatch(b, a)])
