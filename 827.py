s = open(0).read().split()
n = int(s[0])
a = []
c = []
d = {}
i = 1
for _ in range(n):
    k = int(s[i])
    a.append(frozenset(s[i + 1:i + k + 1]))
    c.append(d.setdefault(a[-1], len(d)))
    i += k + 1
g = [[j for j in range(n) if a[i] < a[j] or c[i] == c[j] and i < j] for i in range(n)]
m = [-1] * n


def f(v):
    for u in g[v]:
        if u not in w:
            w.add(u)
            if m[u] < 0 or f(m[u]):
                m[u] = v
                return 1
    return 0


r = n
for v in range(n):
    w = set()
    r -= f(v)
print(r)
