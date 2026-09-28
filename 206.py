n, e, m, *d = map(int, open(0).read().split())
b = [9e9] * (n + 1)
b[1] = 0
r = []
i = 0
for _ in range(m):
    r += [d[i + 1:i + 2 * d[i] + 1]]
    i += 2 * d[i] + 1
r.sort(key=lambda x: x[1])
c = 1
while c:
    c = 0
    for x in r:
        o = 0
        for s, t in zip(x[::2], x[1::2]):
            if o and t < b[s]:
                b[s] = t
                c = 1
            o |= b[s] <= t
print([b[e], -1][b[e] > 8e9])
