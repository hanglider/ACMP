from array import array as Y
v = open(0).read().split()
n = int(v[0])
M = t = G = I = K = 0
V = []
for i in range(n):
    q = i * 5 + 1
    e = v[q] < 'P'
    a, b, c, d = map(int, v[q + 1:q + 5])
    t += e
    M += e << i
    G += c
    I += d
    K += (c - d) * e
    V.append([(a - c) * (s - h) + (b - d) * h for s in range(n + 1) for h in range(n + 1)])
X = (n - t - 1) * G + t * I + K
F = 1 << n
f = Y('h', bytes(2 * F))
for S in range(F - 2, -1, -1):
    j = S.bit_count() * (n + 1) + (S & M).bit_count()
    b = 1 << 30
    m = S ^ F - 1
    while m:
        w = m & -m
        c = V[w.bit_length() - 1][j] + f[S | w]
        if c < b:
            b = c
        m -= w
    f[S] = b
S = 0
R = [0]
for k in range(n):
    j = k * (n + 1) + (S & M).bit_count()
    for y in range(n):
        w = 1 << y
        if not S & w and V[y][j] + f[S + w] == f[S]:
            R.append(y + 1)
            S += w
            break
R.append(0)
print(f[0] + X, *R)
