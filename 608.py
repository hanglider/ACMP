from fractions import Fraction as F
d = list(map(int, open(0).read().split()))
G = [d[:2], d[2:4]]
R = [d[5 + 4 * i:9 + 4 * i] for i in range(d[4])]
e = 1e-9
X = [(a + e, b + e, c - e, d - e) for a, b, c, d in R]
K = []
H = []
for i in range(len(R)):
    for j in range(i):
        a, b = R[i], R[j]
        l, h = max(a[0], b[0]), min(a[2], b[2])
        p, q = max(a[1], b[1]), min(a[3], b[3])
        if l == h and p == q:
            K.append((l, p))
        elif (l == h) ^ (p == q) and l <= h and p <= q:
            H.append((l, p, h, q))
        if l <= h and p <= q:
            X.append((l - 2 * e + e * 3 * (l < h), p - 2 * e + e * 3 * (p < q), h + 2 * e - e * 3 * (l < h), q + 2 * e - e * 3 * (p < q)))
def I(a, b, c, d, B):
    l, h = 0, 1
    for p, q, s, t in (a, c - a, B[0], B[2]), (b, d - b, B[1], B[3]):
        if q:
            s, t = sorted(((s - p) / q, (t - p) / q))
            l = max(l, s)
            h = min(h, t)
        elif not s < p < t:
            return 2
    return l if l < h else 2
def V(x, y):
    return all(I(x, y, a, b, B) > 1 for a, b in G for B in X)
def E(x, y):
    x, y = F(x), F(y)
    for a, b in G:
        if any(I(x, y, a, b, B) < 2 for B in R):
            return 0
        for p, q in K:
            if (a - x) * (q - y) == (b - y) * (p - x) and min(x, a) <= p <= max(x, a) and min(y, b) <= q <= max(y, b):
                return 0
        for p, q, s, t in H:
            if p == s == x == a and max(min(y, b), q) < min(max(y, b), t) or q == t == y == b and max(min(x, a), p) < min(max(x, a), s):
                return 0
    return 1
S = []
for a, b, c, d in R:
    S += [(a, b, c, b), (a, d, c, d), (a, b, a, d), (c, b, c, d)]
    for x, y in (a, b), (a, d), (c, b), (c, d):
        for p, q in G:
            k = 1e9 / max(abs(x - p), abs(y - q))
            u, v = (x - p) * k, (y - q) * k
            t = min([I(x, y, x + u, y + v, B) for B in X] + [1])
            S.append((x, y, x + u * t, y + v * t))
C = [((G[0][0] + G[1][0]) / 2, (G[0][1] + G[1][1]) / 2, 0, 0)]
T = []
for i in range(len(S)):
    a, b, c, d = S[i]
    u, v = c - a, d - b
    for j in range(i):
        x, y, p, q = S[j]
        w, z = p - x, q - y
        D = u * z - v * w
        if D:
            s = ((x - a) * z - (y - b) * w) / D
            t = ((x - a) * v - (y - b) * u) / D
            f = 1e-12 * max(1, abs(u), abs(v))
            g = 1e-12 * max(1, abs(w), abs(z))
            if -f <= s <= 1 + f and -g <= t <= 1 + g:
                x, y = a + s * u, b + s * v
                l = (u * u + v * v)**.5
                m = (w * w + z * z)**.5
                T.append((x, y, 0, 0))
                for h in 1, -1:
                    T += [(x, y, h * u / l, h * v / l), (x, y, h * w / m, h * z / m)]
                    for k in 1, -1:
                        C.append((x, y, h * u / l + k * w / m, h * v / l + k * z / m))
O = len(C)
C += T
Q = []
for i in range(len(C)):
    a, b, u, v = C[i]
    if V(a + u * 1e-7, b + v * 1e-7):
        k = 1e-7
        while i < O and k < 1e4 and V(a + u * k * 2, b + v * k * 2):
            k *= 2
        Q.append((a + u * k, b + v * k))
        if E(*Q[-1]):
            Q = Q[-1:]
            break
if Q:
    print("YES")
    print(*Q[0])
else:
    print("NO")
