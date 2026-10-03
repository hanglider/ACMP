n, m = map(int, input().split())
w = m + 1
g = ''.join(input() + '.' for _ in range(n)) + '.' * w
z = len(g)
d = {1: 'R', -1: 'L', w: 'D', -w: 'U'}
e = [[q for q in (p + 1, p - 1, p + w, p - w) if g[q] == '?'] if g[p] == '?' else [] for p in range(z)]
a = [-1] * z
for p in range(z):
    if e[p] and a[p] < 0:
        a[p] = e[p][0]
        b = [p]
        for x in b:
            for q in e[x]:
                if a[q] < 0:
                    a[q] = x
                    b.append(q)
k = [p for p in range(z) if e[p] and (p // w + p % w) % 2 < 1]
t = [-1] * z
for u in k:
    for q in e[u]:
        if t[q] < 0:
            t[q] = u
            t[u] = q
            break
f = 1
while f:
    f = 0
    v = [0] * z
    for u in k:
        if t[u] < 0:
            v[u] = 1
            s = [(u, iter(e[u]))]
            y = []
            while s:
                x, i = s[-1]
                for q in i:
                    r = t[q]
                    y.append(q)
                    if r < 0:
                        for (x, _), q in zip(s, y):
                            t[x] = q
                            t[q] = x
                        f = 1
                        s = []
                        break
                    if not v[r]:
                        v[r] = 1
                        s.append((r, iter(e[r])))
                        break
                    y.pop()
                else:
                    s.pop()
                    y[-1:] = []
print('\n\n'.join('\n'.join(''.join(d[a[p] - p] if e[p] else g[p] for p in range(i * w, i * w + m)) for i in range(n)) for a in (a, [t[p] if t[p] + 1 else e[p] and e[p][0] for p in range(z)])))
