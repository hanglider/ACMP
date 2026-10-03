from functools import lru_cache
from itertools import groupby
s = input()


@lru_cache(None)
def h(t):
    r = [(c, len(list(g))) for c, g in groupby(t)]

    @lru_cache(None)
    def f(i, j, e):
        if i > j:
            return 0
        c, n = r[i]
        n += e
        return min([(e < 1 or n < 3) * max(1, 3 - n) + f(i + 1, j, 0)] + [f(i + 1, k - 1, 0) + f(k, j, min(n, 3)) for k in range(i + 1, j + 1) if r[k][0] == c])
    return f(0, len(r) - 1, 0)


@lru_cache(None)
def g(t, d):
    if not t:
        return ' '
    if h(t) > d:
        return ''
    for i in range(len(t)):
        c = t[i]
        if i and t[i - 1] == c:
            continue
        l = t[:i] + c
        r = t[i:]
        while l and r and l[-1] == r[0]:
            k = r[0]
            x = l.rstrip(k)
            y = r.lstrip(k)
            if len(x + y) + 3 > len(l + r):
                break
            l = x
            r = y
        x = g(l + r, d - 1)
        if x:
            return c + str(i) + ' ' + x


t = h(s)
while not g(s, t):
    t += 1
print(t, g(s, t).strip())
