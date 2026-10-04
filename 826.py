s = open(0).read().split()
n = int(s[0])
g = [[] for _ in range(n + 1)]
for i in range(1, 2 * n - 1, 2):
    u = int(s[i])
    v = int(s[i + 1])
    g[u].append(v)
    g[v].append(u)
m = -10**9
d = [[(c == "I") if c in s[2 * n - 2 + v] else m for c in "IBV"] for v in range(n + 1)]
o = [1]
p = [0] * (n + 1)
for v in o:
    for u in g[v]:
        if u != p[v]:
            p[u] = v
            o.append(u)
for v in o[:0:-1]:
    a, b, c = d[v]
    w = d[p[v]]
    w[0] += max(b, c)
    w[1] += max(a, c)
    w[2] += max(a, b)
r = max(d[1])
print(+r if r >= 0 else -1)
