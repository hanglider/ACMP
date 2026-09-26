t = [*map(int, open('input.txt').read().split())]
n = t[0]
w = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(2, len(t), 3):
    a, b, c = t[i:i + 3]
    w[a][b] = max(w[a][b], c)
E = [[b for b in range(n + 1) if w[a][b]] for a in range(n + 1)]
r = []
for v in range(2, n + 1):
    g = [0] * (n + 1)
    z = g[:]
    z[1] = 1
    s = [1]
    for a in s:
        if a != v:
            for b in E[a]:
                g[b] += 1
                if not z[b]:
                    z[b] = 1
                    s.append(b)
    d = [0] * (n + 1)
    q = [1] * (g[1] < 1)
    for a in q:
        if a != v:
            for b in E[a]:
                d[b] = max(d[b], d[a] + w[a][b])
                g[b] -= 1
                if not g[b]:
                    q.append(b)
    r.append(d[v] if v in q else -1)
print(*r)