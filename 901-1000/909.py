import re
from bisect import bisect
r = open(0).read().split()
t = str.maketrans('-SX', '011')
p = []
f = []
a = []
h = w = 0
for s in r[2:]:
    n = len(p)
    x = [m.start() for m in re.finditer('[XS]+', s)]
    g = re.findall('[XS]+', s)
    f += [('S' in y) + 2 * ('X' in y) for y in g]
    p += range(n, n + len(g))
    c = int(s.translate(t), 2)
    for m in re.finditer('1+', bin(c & w | 1 << len(s))[3:]):
        j = m.start()
        u = h + bisect(a, j) - 1
        v = n + bisect(x, j) - 1
        while p[u] != u:
            p[u] = u = p[p[u]]
        while p[v] != v:
            p[v] = v = p[p[v]]
        p[max(u, v)] = min(u, v)
    a = x
    h = n
    w = c
for k in range(len(p)):
    p[k] = p[p[k]]
    f[p[k]] |= f[k]
o = [0] * 4
for k in range(len(p)):
    if p[k] == k:
        o[f[k]] += 1
print(o[1], o[3], o[2])
