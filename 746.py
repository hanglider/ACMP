n, m, *d = map(int, open(0).read().split())
g = [0] * (n + 1)
for u, v in zip(d[::2], d[1::2]):
    g[u] |= 1 << v
    g[v] |= 1 << u
r = 0
for i in range(n + 1):
    for j in range(i):
        c = bin(g[i] & g[j]).count("1")
        r += c * c - c
print(r // 4)
