n, m, *e = map(int, open(0).read().split())
p = list(range(n + 1))
d = [0] * (n + 1)
s = {}
def r(u):
    while p[u] - u:
        p[u] = u = p[p[u]]
    return u
for u in e:
    d[u] += 1
for u, v in zip(e[::2], e[1::2]):
    p[r(u)] = r(v)
for u in set(e):
    s[r(u)] = s.get(r(u), 0) + d[u] % 2
print(sum(max(2, x) // 2 for x in s.values()))
