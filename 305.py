n, m, k, *a = map(int, open(0).read().split())
s = list(zip(*[iter(a)] * 4))
h = [0] * (m + 1)
r = 0
for y in range(1, n + 1):
    t = []
    for x in range(m + 1):
        if x < m:
            h[x] = (h[x] + 1) * all(y < p - 1 or y > q + 1 or x < c - 2 or x > d for p, c, q, d in s)
        j = x
        while t and t[-1][1] >= h[x]:
            j, v = t.pop()
            r = max(r, v * (x - j))
        t.append((j, h[x]))
print(r)
