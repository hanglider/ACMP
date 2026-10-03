import re
from bisect import bisect
n, k, l, *a = map(int, open(0).read().split())
m = n
j = 0
x = []
y = []
z = []
while m >= k:
    q = m // k
    s = (m - q * k) // q + 1
    x += [j]
    y += [m]
    z += [q]
    m -= s * q
    j += s
def T(j):
    i = bisect(x, j) - 1
    return n - y[i] + (j - x[i]) * z[i]
o = [0] * l
v = {}
def g(i, p, j):
    r = p // k
    if r:
        d = p - r * k
        c = d % r
        if c:
            v.setdefault(r, []).append((i, c, j + d // r + 1))
        else:
            o[i] = T(j + d // r) + r
w = []
for i in range(l):
    if a[i] // k > k:
        w += [i]
    else:
        g(i, a[i], 0)
j = 0
while w:
    f = len(w)
    X = int.from_bytes(b''.join(a[i].to_bytes(8, 'little') for i in w), 'little')
    O = int.from_bytes((b'\1' + bytes(7)) * f, 'little')
    L = O * (2**24 - 1)
    C = O * (2**24 - 1 - k)
    Y = O * (2**36 - 1)
    M = -(-2**36 // k)
    N = O * (2**36 - M)
    A = O << 36
    h = f
    while A and (h * 2 > f or h < 64):
        P = X * M
        Q = P >> 36 & L
        D = A & ~((P & Y) + N)
        if j % 8 < 1:
            D |= A & ~((Q + C) << 12)
        if D:
            A ^= D
            b = (X | D << 27).to_bytes(8 * f, 'little')
            for t in re.finditer(b'\x80', b):
                s = t.start() - 7
                if s % 8 < 1:
                    g(w[s >> 3], int.from_bytes(b[s:s + 3], 'little'), j)
                    h -= 1
            D = ~((D >> 36) * (2**64 - 1))
            X &= D
            Q &= D
        X -= Q
        j += 1
    b = X.to_bytes(8 * f, 'little')
    u = []
    for s in range(f):
        p = int.from_bytes(b[8 * s:8 * s + 8], 'little')
        if p:
            a[w[s]] = p
            u += [w[s]]
    w = u
if v:
    M = max(v)
    t = [i & -i for i in range(M + 1)]
    u = [0] * (M + 2)
    B = 1 << M.bit_length()
    def R(r):
        p = 0
        b = B
        while b:
            if p + b <= M and t[p + b] <= r:
                p += b
                r -= t[p]
            b >>= 1
        return p + 1
    def H(i, c):
        while i <= M:
            u[i] += c
            i += i & -i
    def V(i):
        s = 0
        while i:
            s += u[i]
            i -= i & -i
        return s
    D = {}
    G = 0
    e = 0
    for r in range(M, 0, -1):
        for i, c, h in v.get(r, ()):
            p = R((e + c) % r)
            D.setdefault(p, []).append((i, h - V(p) - G))
        p = R(e)
        for i, h in D.get(p, ()):
            o[i] = T(h + V(p) + G) + r
        i = p
        while i <= M:
            t[i] -= 1
            i += i & -i
        s = r - 1
        if s < 1:
            break
        e = (e - k) % s
        G += (k - 1) // s
        b = (k - 1) % s
        if b:
            c = R((e + 1) % s)
            h = R((e + b) % s)
            H(c, 1)
            H(h + 1, -1)
            if c > h:
                H(1, 1)
print('\n'.join(map(str, o)))
