from math import lcm
n, k, *a = map(int, open(0).read().split())
d = {1: 1}
for p in {x for x in a if a.count(x) % 2}:
    for l, v in list(d.items()):
        m = lcm(l, p)
        if m <= n:
            d[m] = d.get(m, 0) - 2 * v
            if not d[m]:
                del d[m]
print((n - sum(v * (n // l) for l, v in d.items())) // 2)
