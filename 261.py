from bisect import *
n, m, k, *s = open(0).read().split()
m = int(m)
a = [0] + list(map(int, s[:m]))
s = s[m:]
def f(l, r, t):
    c = (r - l) * a[t]
    if t == m:
        return c
    b = []
    p = s[l][:t]
    for d in range(int(k)):
        j = bisect_left(s, p + chr(49 + d), l, r)
        if j == l:
            return c
        b += f(l, j, t + 1) - (j - l) * a[t],
        l = j
    return c + min(b)
print(f(0, len(s), 0))
