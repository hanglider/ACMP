*d, s, t = open(0).read().split()
r = {s: 0}
q = [s]
for x in q:
    for a, b in zip(d[1::3], d[3::3]):
        if a == x and b not in r:
            r[b] = r[x] + 1
            q += b,
print(r.get(t, -1))
