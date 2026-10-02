from operator import sub
n, m, *a = open(0).read().split()
n = int(n)
m = int(m)
k = int(a[n + m])
q = a[n + m + 1:n + m + 1 + k]
f = {a[n + m + 2 + k + i] for i in range(int(a[n + m + 1 + k]))}
g = [(x, y, str(i + 1) in f) for i, x in enumerate(a[:n]) for y in a[n:n + m]]
c = len(g)
w = [[0] * (c + 1)]
for s in q:
    x, y, z = s.split('-')
    w.append([0] + [-int(z) * h if len(x) == len(i) and len(y) == len(j) and all(e in '?' + d for e, d in zip(x + y, i + j)) else 10**9 for i, j, h in g])
u = [0] * (k + 1)
v = [0] * (c + 1)
p = [0] * (c + 1)
r = [0] * (c + 1)
for i in range(1, k + 1):
    p[0] = i
    j = 0
    b = [10**18] * (c + 1)
    t = []
    l = v[:]
    while p[j]:
        t.append(j)
        l[j] = -10**30
        b[j] = 10**18
        o = p[j]
        e = list(map(sub, w[o], l))
        h = u[o]
        for x in [x for x in range(c + 1) if e[x] - h < b[x]]:
            b[x] = e[x] - h
            r[x] = j
        d = min(b)
        y = b.index(d)
        b = [z - d for z in b]
        for x in t:
            u[p[x]] += d
            v[x] -= d
            b[x] = 10**18
        j = y
    while j:
        p[j] = p[r[j]]
        j = r[j]
print(v[0])
