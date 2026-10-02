r = open(0).read().split()
n = int(r[0])
w = n + 1
a = []
for i in range(n):
    a += r[1 + i * n:w + i * n] + ['0']
S = dict.fromkeys([*range(-w, 0), *range(n * w, n * w + w), *range(n, n * w, w)])
f = {k: k for k in range(n * w) if a[k] != '0'}
while f:
    S.update(f)
    g = {}
    for k, s in f.items():
        for m in k - 1, k + 1, k - w, k + w:
            if m not in S:
                g[m] = s if g.get(m, s) == s else -1
    f = g
for i in range(n):
    print(*[a[S.get(i * w + j, -1)] for j in range(n)])
