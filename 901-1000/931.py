from itertools import combinations as C
n, *z = map(int, open(0).read().split())
p = list(zip(z[::2], z[1::2]))
m = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
e = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2
g = lambda a, b, c, d: e(a, b) * m(a, c, d) - e(a, c) * m(a, b, d) + e(a, d) * m(a, b, c)
for t in C(p[:5], 3):
    r = [i for i in range(n) if g(*t, p[i])]
    s = [p[i] for i in r[:3]]
    if m(*t) and (len(r) < 3 or m(*s) and not any(g(*s, p[i]) for i in r)):
        print(*(i + 1 for i in range(n) if i not in r))
        print(*[i + 1 for i in r] or [1])
        exit()
k = n // 2
print(*range(1, k + 1))
print(*range(k + 1, n + 1))
