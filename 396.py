from bisect import *
from array import *
n, m = map(int, input().split())
a = array('i')
b = array('i')
for _ in range(n):
    x, y = sorted(map(int, input().split()))
    a.append(x)
    b.append(y)
a = array('i', sorted(a))
b = array('i', sorted(b))
for x in map(int, input().split()):
    print(bisect(a, x) - bisect_left(b, x), end=' ')
