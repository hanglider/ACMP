n, m, *a = map(int, open(0).read().split())
r = []
for c, p in ("R", [(x - 1) // m for x in a[::m]]), ("C", [(x - 1) % m for x in a[:m]]):
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], j
            r += [f"{c} {i + 1} {j + 1}"]
print(len(r), *r, sep="\n")
