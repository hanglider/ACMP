from math import cos, sin, pi, atan2, hypot, acos
A = list(map(int, open(0).read().split()))
r = A[0]
l = A[1]
m = A[2]
t = 2 * pi * r / l
def f(a):
    b = a + t
    c = lambda x: (x - a) % (2 * pi) <= t
    p = l * max(0, 1 if c(0) else max(cos(a), cos(b)))
    q = l * min(0, -1 if c(pi) else min(cos(a), cos(b)))
    u = l * max(0, 1 if c(pi / 2) else max(sin(a), sin(b)))
    v = l * min(0, -1 if c(3 * pi / 2) else min(sin(a), sin(b)))
    return p - q, u - v
E = lambda z: z[0][0] * (z[1][1] * z[2][2] - z[1][2] * z[2][1]) - z[0][1] * (z[1][0] * z[2][2] - z[1][2] * z[2][0]) + z[0][2] * (z[1][0] * z[2][1] - z[1][1] * z[2][0])
def g(p, q):
    M = [[cos(x), sin(x), 1] for x in p]
    d = E(M)
    a = E([[q[i], M[i][1], M[i][2]] for i in range(3)])
    b = E([[M[i][0], q[i], M[i][2]] for i in range(3)])
    c = E([[M[i][0], M[i][1], q[i]] for i in range(3)])
    return a / d, b / d, c / d
s = set()
for k in range(4):
    z = k * pi / 2
    for x in (z, z - t, z - t / 2, z + (pi - t) / 2):
        s.add(x % (2 * pi))
B = sorted(s)
B.append(B[0] + 2 * pi)
C = B[:]
for i in range(len(B) - 1):
    u = B[i]
    v = B[i + 1]
    if v - u < 1e-9:
        continue
    P = [u + (v - u) * j / 4 for j in (1, 2, 3)]
    W = [f(x) for x in P]
    a, b, c = g(P, [w[0] for w in W])
    x = atan2(b, a)
    for k in range(-2, 4):
        y = x + k * pi
        if u < y < v:
            C.append(y)
    a, b, c = g(P, [w[1] for w in W])
    h = hypot(a, b)
    if h > 1e-12:
        o = (m - c) / h
        if abs(o) <= 1:
            x = atan2(b, a)
            q = acos(o)
            for k in range(-2, 4):
                for y in (x + q + 2 * k * pi, x - q + 2 * k * pi):
                    if u < y < v:
                        C.append(y)
z = 1e18
for x in C:
    a, b = f(x)
    if b <= m + 1e-6:
        z = min(z, a)
print("%.6f" % z)
