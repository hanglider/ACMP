m, n, *a = map(int, open(0).read().split())
r = range(m)
d = a[n - 1::n]
p = []
for j in range(n - 2, -1, -1):
    t = [min(range(max(i - 1, 0), min(i + 2, m)), key=lambda k: d[k]) for i in r]
    p = [t] + p
    d = [a[i * n + j] + d[t[i]] for i in r]
s = min(d)
i = d.index(s)
o = [i + 1]
for t in p:
    i = t[i]
    o += [i + 1]
print(*o)
print(s)
