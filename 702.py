n, *a = map(int, open(0).read().split())
s = set()
for i in range(0, 4 * n, 4):
    s |= {x * 101 + y for x in range(a[i], a[i + 2]) for y in range(a[i + 1], a[i + 3])}
m = 0
while s:
    q = [s.pop()]
    c = 0
    while q:
        p = q.pop()
        c += 1
        for d in 1, -1, 101, -101:
            if p + d in s:
                s.remove(p + d)
                q += p + d,
    m = max(m, c)
print(m)
