from math import gcd
from functools import cache
n = int(input())
a = list(map(int, input().split()))
r = []
for x in a:
    e = [y - x for y in a]
    @cache
    def h(g):
        m = list(map(gcd, [g] * n, e))
        return set(m) - {1, g}, m.count(g)
    @cache
    def w(g, c):
        s, k = h(g)
        return k > c and not w(g, c + 1) or any(not w(d, c + 1) for d in s)
    if all(w(abs(y - x), 2) for y in a if abs(y - x) > 1):
        r += [x]
print(len(r))
print(*r)
