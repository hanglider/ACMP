from itertools import *
from operator import *
from array import array
n, *a = map(int, open(0).read().split())
z = 2**64
u = (z**32 - 1) // (z - 1)
k = u * (2**32 - 1)
e = [sum((z - 1) * z**i for i in range(32) if i >> b & 1) for b in range(5)]
o = [u] * 94
f = [o] * n
g = [[] for _ in f]
t = 1
q = lambda v: array('Q', b''.join(map(int.to_bytes, map(and_, v, repeat(k)), repeat(256), repeat('little')))).tolist()
h = lambda v, r: [*map(and_, v[:r % 94 + 1], repeat(k % z**(r // 94 + 1))), *map(and_, v[r % 94 + 1:], repeat(k % z**(r // 94)))]
for l, r in zip(a[-2::-2], a[::-2]):
    v = f.pop()
    for y in g.pop():
        v = [w * c - ((w & e[0]) + (w & e[1]) * 2 + (w & e[2]) * 4 + (w & e[3]) * 8 + (w & e[4]) * 16) * 94 for w, c in zip(h(v, y), range(y + 1, y - 93, -1))]
    if l < 0 and v is o:
        g[-l - 1].append(r)
        continue
    s = [*accumulate(h(v, r)[::-1])][::-1]
    s = [*map(add, s, repeat(s[0] // (z - 1)))]
    if l < 0:
        p = f[-l - 1]
        if p is not o:
            b = array('Q', [*map(mul, q(p), q(s))]).tobytes()
            s = [int.from_bytes(b[i:i + 256], 'little') for i in range(0, 24064, 256)]
        f[-l - 1] = s
    else:
        t = t * (s[l % 94] >> l // 94 * 64) % 2**32
print(t)
