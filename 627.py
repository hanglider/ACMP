from collections import Counter as K
w, n, *i = open(0).read().split()
n = int(n)
C = K(w)
p = {x for x in i[:n] if not K(x) - C}
q = {x for x in i[n + 1:] if not K(x) - C}
c = len(p & q)
a = len(p) - c
b = len(q) - c
for d in a - b + c % 2, max(a - b - c, (c - a) % 2 - b), min(a + c - b, a + (c - b) % 2):
    print((d > 0) + 2 * (d < 0))
