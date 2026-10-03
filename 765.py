n, *g = open(0).read().split()
d = {(i, j): c for i, r in enumerate(g) for j, c in enumerate(r)}
k = 0
for p in d:
    if d[p] == 'B':
        s = [p]
        e = set()
        d[p] = 0
        for i, j in s:
            for q in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                c = d.get(q)
                if c == 'B':
                    d[q] = 0
                    s += q,
                if c == '.':
                    e.add(q)
        k += len(e) == 1
print(k)
