d = list(map(int, open('input.txt').read().split()))
n = d[0]
m = d[1]
r = d[2:2 + n]
c = d[2 + n:2 + n + m]
z = d[2 + n + m:]
s = 0
for i in range(n):
    for j in range(m):
        v = z[i * m + j]
        if v >= 0:
            r[i] -= v
            c[j] -= v
            s += v
if min(r) < 0 or min(c) < 0:
    print(-1)
else:
    t = n + m + 1
    g = [[0] * (t + 1) for _ in range(t + 1)]
    for i in range(n):
        g[0][i + 1] = r[i]
    for j in range(m):
        g[n + 1 + j][t] = c[j]
    for i in range(n):
        for j in range(m):
            if z[i * m + j] < 0:
                g[i + 1][n + 1 + j] = 10**9
    while 1:
        p = [-1] * (t + 1)
        p[0] = 0
        q = [0]
        for u in q:
            for v in range(t + 1):
                if g[u][v] > 0 and p[v] < 0:
                    p[v] = u
                    q.append(v)
        if p[t] < 0:
            break
        a = 10**9
        v = t
        while v:
            a = min(a, g[p[v]][v])
            v = p[v]
        v = t
        while v:
            g[p[v]][v] -= a
            g[v][p[v]] += a
            v = p[v]
        s += a
    print(s)
