from array import *
from itertools import *
t = open('input.txt').read().split()
L, W, n = map(int, t[:3])
a = [*map(int, t[3:3 + n])]
b = [*map(int, t[4 + n:])]
m = len(b)
z = n + m - 1
D = [array('d', [(W * W + (a[j] - b[T - j])**2)**.5 + a[j] + b[T - j] for j in range(max(0, T - m + 1), min(n, T + 1))]) for T in range(z)]
L += 1e-6
I = array('d', [9e9])
r = 1
h = lambda Q: [*chain(*(accumulate(Q[k:k + r], min) for k in range(0, len(Q), r)))]
for S in range(z):
    u = max(0, S - m + 1)
    x = [L + 2 * (a[i] + b[S - i]) - y for i, y in zip(range(u, n), D[S])]
    s = u
    while S + r <= z:
        c = max(0, S + r - m)
        P = I * (c - s) + D[S + r - 1][max(s - c, 0):] + I * r
        if r < 20:
            w = map(min, P, *[P[k:] for k in range(r)])
        else:
            P += I * (-len(P) % r)
            w = map(min, h(P[::-1])[::-1], h(P)[r - 1:])
        y = [*map(float.__le__, w, x[s - u:])]
        if 1 not in y:
            break
        s += y.index(1)
        r += 1
print(r * (r > 1))