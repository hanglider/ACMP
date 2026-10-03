from itertools import accumulate
from operator import sub
a, b = open(0).read().split()
d = {'A': 1, 'C': 2048, 'G': 2048**2, 'T': 2048**3}
p = [0, *accumulate(d[c] for c in a)]
q = [0, *accumulate(d[c] for c in b)]
for l in range(min(len(a), len(b)), 0, -1):
    x = list(map(sub, p[l:], p))
    y = list(map(sub, q[l:], q))
    s = set(x) & set(y)
    if s:
        v = s.pop()
        print(l)
        print(x.index(v) + 1, y.index(v) + 1)
        break
else:
    print(0)
