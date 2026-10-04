k, m, *n = map(int, open(0).read().split())
c = {}
f = []
r = n[0]
for i in range(m - 1):
    v = n[i] // (n[i] - n[i + 1])
    if c.get(v):
        c[v] -= 1
    else:
        f += [v]
        r //= v
    c[v - 1] = c.get(v - 1, 0) + 1
print(*(f + [r] + [1] * k)[:k])
