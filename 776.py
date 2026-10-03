s = list(map(int, open(0).read().split()))
n, m, x, y, k, d = s[:6]
w = n + 2
z = w * (m + 2)
g = [10**6] * z
for i in range(m):
    g[w * i + w + 1:w * i + w + n + 1] = s[6 + i * n:6 + i * n + n]
o = (1, -1, w, -w)
T = {}
for a in 1, w:
    t = [g]
    for l in range(7):
        p = t[-1]
        h = a << l
        t.append([max(p[i], p[i + h]) if i + h < z else p[i] for i in range(z)])
    T[a] = T[-a] = t
P = [[list(range(z)) for _ in range(k + 2)] for _ in o]


def f(p, j):
    r = j
    while p[r] != r:
        r = p[r]
    while p[j] != r:
        p[j], j = r, p[j]
    return r


b = [k + 1] * z


def u(j, c):
    for v in range(c, min(b[j], k + 1)):
        for e in range(4):
            P[e][v][j] = j + o[e]
    b[j] = c


for i in range(z):
    if g[i] == 0:
        for e in range(4):
            for v in P[e]:
                v[i] = i + o[e]
u(w + 1, 0)
q = [w + 1]
r = 0
e = y * w + x
while q and b[e] > k:
    a = []
    for v in q:
        i, c = v % z, v // z
        for s in o:
            j = i + s
            if 0 < g[j] < 10**6 and abs(g[i] - g[j]) < 2 and b[j] > c:
                u(j, c)
                a.append(c * z + j)
            if c < k:
                p = P[o.index(s)][c + 1]
                t = T[s]
                j = f(p, i + s)
                while 1:
                    l = (j - i) // s
                    h = (l + 1).bit_length() - 1
                    if s > 0:
                        M = max(t[h][i], t[h][j - (2**h - 1) * s])
                    else:
                        M = max(t[h][j], t[h][i + (2**h - 1) * s])
                    if l + M - g[i] > d:
                        break
                    if l + 2 * M - g[i] - g[j] <= d:
                        u(j, c + 1)
                        a.append(c * z + z + j)
                    j = f(p, j + s)
    q = a
    r += 1
print(r if b[e] <= k else 'IMPOSSIBLE')
