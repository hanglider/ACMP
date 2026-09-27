from collections import Counter
t = [*map(int, open(0).read().split())]
n = t[0]
Q = [t[i:i + 3] for i in range(1, 3 * n, 3)]


def f(A, B):
    x, y, l = A
    u, v, m = B
    a, b = max(x, u), min(x + l, u + m)
    c, d = max(y, v), min(y + l, v + m)
    w = b - a
    h = d - c
    if w <= 0 or h <= 0:
        return hash((l, l))
    if w == h == l:
        return 0
    if w == l:
        return hash((l, l - h))
    if h == l:
        return hash((l - w, l))
    return hash((l, a - x, c - y, w, h))


H = [[f(A, B) for B in Q] for A in Q]
r = n * n - n + sum(x * x for x in Counter(H[i][j] for i in range(n) for j in range(n) if i != j).values())
for s in range(n):
    R = Counter(H[s][j] for j in range(n) if j != s)
    C = Counter(H[i][s] for i in range(n) if i != s)
    r -= sum(x * x for x in R.values()) + sum(x * x for x in C.values()) + 2 * sum(R[z] * C[z] for z in R)
    r += sum(H[s][j] == H[j][s] for j in range(n) if j != s)
print(r)