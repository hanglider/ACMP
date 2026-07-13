from math import comb as c
d = open(0).read().split()
n = int(d[0])
r = 1
for i in range(n):
    a, b = map(int, d[1 + i].split(":"))
    w = max(a, b)
    l = min(a, b)
    m = 15 if i == 4 else 25
    if w == m:
        r *= c(w - 1 + l, l)
    else:
        r *= c(2 * (m - 1), m - 1) * 2**(l - m + 1)
print(r)
