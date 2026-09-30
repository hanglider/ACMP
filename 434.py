from array import *
from itertools import *
from operator import *
H = 1 << 31
M = 2 * H - 1
n = int(input())
s = []
f = u = None
for i in range(n + 1):
    x, y = map(int, input().split()) if i < n else f
    f = f or (x, y)
    if x == u:
        s += [x << 64 | min(y, w) + H << 32 | max(y, w) + H]
    u, w = x, y
s.sort()
X = array("q", map(rshift, s, repeat(64)))
L = array("q", map(sub, map(and_, map(rshift, s, repeat(32)), repeat(M)), repeat(H)))
U = array("q", map(sub, map(and_, s, repeat(M)), repeat(H)))
del s
q = array("b", map(ne, X, X[1:]))
B = array("q", compress(map(max, accumulate(L, min), array("q", accumulate(L[::-1], min))[-2::-1]), q))
T = array("q", compress(map(min, accumulate(U, max), array("q", accumulate(U[::-1], max))[-2::-1]), q))
X = array("q", compress(X, q)) + X[-1:]
o = array("q")
i = 0
for c, g in groupby(B):
    o.extend((X[i], c))
    i += len(list(g))
    o.extend((X[i], c))
for c, g in groupby(T[::-1]):
    o.extend((X[i], c))
    i -= len(list(g))
    o.extend((X[i], c))
print(len(o) // 2)
for i in range(0, len(o), 9998):
    print(*map("%d %d".__mod__, zip(o[i:i + 9998:2], o[i + 1:i + 9998:2])), sep="\n")
