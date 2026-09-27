t = [*map(int, open(0).read().split())]
k = t[1]
w = 51 - k
G = {}
for x, y in zip(t[2::2], t[3::2]):
    z = G.setdefault((max(1, y - k + 1), min(y, w)), [w, 1])
    z[0] = min(z[0], min(x, w))
    z[1] = max(z[1], max(1, x - k + 1))
W = [(E, D, a, b) for (E, D), (a, b) in G.items()]
M = max(E for E, D, a, b in W)
d = {(1, 0): 0}
o = 9e9
for y in range(1, w + 1):
    A = [(i, a, b) for i, (E, D, a, b) in enumerate(W) if E <= y <= D]
    n = {}
    for (s, m), c in d.items():
        m |= sum(3 << 2 * i for i, (E, D, a, b) in enumerate(W) if E == y)
        for l in {s} | {a for i, a, b in A if a < s}:
            for r in {s} | {b for i, a, b in A if b > s}:
                u = m
                for i, a, b in A:
                    u &= ~((a >= l) + 2 * (b <= r) << 2 * i)
                for e, g in (r, c + s - l + r - l), (l, c + r - s + r - l):
                    if g < n.get((e, u), 9e9):
                        n[e, u] = g
    for (e, u), c in n.items():
        if y >= M and not u:
            o = min(o, c + y - 1)
    f = sum(3 << 2 * i for i, (E, D, a, b) in enumerate(W) if D == y)
    d = {q: c for q, c in n.items() if not q[1] & f}
print(o)