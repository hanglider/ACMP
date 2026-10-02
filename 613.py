from functools import cache
n, r, w, *q = open(0).read().split()
n = int(n)
d = len(set(w))
@cache
def f(s, u, t):
    j = len(s)
    i = 26 - d + j - u
    a = float(q[t])**(1 / (sum(s) - j + 1))
    p = (1 - a) * j / i + a * (1 - 1 / i)**(i - j)
    z = p / j * sum(f(s[:k] + s[k + 1:], u, t) if j > 1 else t == int(r) - 1 for k in range(j))
    if i > j:
        z += (1 - p) * f(s, u + 1, (t + 1) % n)
    return z
print(f(tuple(sorted(w.count(c) for c in set(w))), 0, 0))
