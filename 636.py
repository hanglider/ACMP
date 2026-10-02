from collections import Counter
n, *d = map(int, open(0).read().split())
p = list(zip(d[::2], d[1::2]))
v = {x: min(i, n - i) for i, x in enumerate(p)}
c = Counter(d[::2])
for a in c:
    k = c[a]
    for s in 1, -1:
        for j in range(2 * k)[::s]:
            x = a, j % k + 1
            v[x] = min(v[x], v[a, (j - s) % k + 1] + 1)
print(*(v[x] for x in p))
