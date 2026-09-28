from math import perm
n, k, *a = map(int, open(0).read().split())
s = [*range(1, n + 1)]
r = 1
for i, x in enumerate(a):
    r += s.index(x) * perm(n - i - 1, k - i - 1)
    s.remove(x)
print(r)
