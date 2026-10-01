n, m, *e = map(int, open(0).read().split())
c = [1 << i for i in range(n)]
g = c[:]
for a, b in zip(*[iter(e)] * 2):
    c[a - 1] |= 1 << b - 1
    g[b - 1] |= 1 << a - 1
for k in range(n):
    for i in range(n):
        if c[i] >> k & 1:
            c[i] |= c[k]
d = []
for v in range(n):
    x = 0
    for u in range(n):
        if g[v] >> u & 1:
            x |= c[u]
    d += x,
f = (1 << n) - 1
r = 0
for s in range(n):
    t = q = c[s]
    k = 0
    while t < f:
        x = 0
        while q:
            b = q & -q
            x |= d[b.bit_length() - 1]
            q ^= b
        q = x & ~t
        t |= x
        k += 1
    r = max(r, k)
print(r)
