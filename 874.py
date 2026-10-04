n, k, m, *e = map(int, open(0).read().split())
s = 0
for i in range(1 << m):
    c = list(range(n + 1))
    for _ in c:
        for j in range(m):
            if i >> j & 1:
                u = e[2 * j]
                v = e[2 * j + 1]
                c[u] = c[v] = min(c[u], c[v])
    s += (-1)**bin(i).count('1') * k**(len(set(c)) - 1)
print(s)
