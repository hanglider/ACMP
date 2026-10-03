from operator import add
n, m, *a = map(int, open(0).read().split())
a = [a[i * m:i * m + m] for i in range(n)]
r = [0, 0]
w = 0
while any(map(any, a)):
    t = a
    if w:
        d = a[-1]
        t = [d]
        for x in a[-2::-1]:
            d = [*map(add, x, map(max, [0] + d, d, d[1:] + [0]))]
            t = [d] + t
    k = m
    for i in range(n):
        k = max(range(max(k - 1, 0), min(k + 2, m)) if i else range(m), key=lambda j: (t[i][j], j))
        r[w] += a[i][k]
        a[i][k] = 0
    w = 1 - w
print(*r)
