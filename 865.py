from operator import add
n, *w, t = open(0).read().split()
u = t.upper()
m = len(u)
r = {c: [min((ord(c) - ord(k)) % 26, (ord(k) - ord(c)) % 26) for k in u] for c in map(chr, range(65, 91))}
s = {}
for v in {x.upper() for x in w}:
    if len(v) <= m:
        c = [0] * (m - len(v) + 1)
        for j, a in enumerate(v):
            c = list(map(add, c, r[a][j:]))
        s[v] = c
f = [0] + [m * 26] * m
p = [0] * (m + 1)
for i in range(m):
    if f[i] < m * 26:
        for v in s:
            k = i + len(v)
            if k <= m and f[i] + s[v][i] < f[k]:
                f[k] = f[i] + s[v][i]
                p[k] = v
if f[m] == m * 26:
    print(-1)
else:
    k = m
    e = ''
    while k:
        e = p[k] + e
        k -= len(p[k])
    print(''.join(a if b < 'a' else a.lower() for a, b in zip(e, t)))
