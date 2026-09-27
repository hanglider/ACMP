n, m, *a = map(int, open(0).read().split())
def f(l):
    d = {0: 0}
    for x in l:
        e = {}
        for s, c in d.items():
            for k in 0, 1, 2:
                e[s + k * x] = min(e.get(s + k * x, 99), c + k)
        d = e
    return d
p = f(a[:7])
q = f(a[7:])
r = min((c + p[n - s] for s, c in q.items() if n - s in p), default=0)
print(-1 if 2 * sum(a) < n else r)
