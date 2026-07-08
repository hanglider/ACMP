import sys
sys.setrecursionlimit(9999)
d = open('INPUT.TXT').read().split()
n = int(d[0])
h = [[] for i in range(n + 1)]
for i in range(2, n + 1):
    h[int(d[i - 1])].append(i)
W = 10**6
s = [0] * (n + 1)
m = {}
q = []
for v in range(n, 0, -1):
    t = tuple(sorted(s[u] for u in h[v]))
    if t not in m:
        m[t] = len(q)
        q.append(t)
    s[v] = m[t]

def C(a, b):
    if b > a:
        return 0
    r = 1
    for i in range(min(b, a - b)):
        r = r * (a - i) // (i + 1)
        if r >= W:
            return W
    return r

def F(k):
    g = []
    for t in q:
        r = k
        j = 0
        while j < len(t):
            e = j
            while e < len(t) and t[e] == t[j]:
                e += 1
            r = min(W, r * C(g[t[j]], e - j))
            j = e
        g.append(r)
    return g

a = 1
b = n
while a < b:
    c = (a + b) // 2
    if F(c)[s[1]] > 0:
        b = c
    else:
        a = c + 1
g = F(a)
z = [0] * (n + 1)

def U(a, b, r):
    o = []
    x = 0
    while b:
        w = C(a - x - 1, b - 1)
        if r < w:
            o.append(x)
            b -= 1
        else:
            r -= w
        x += 1
    return o

def A(v, t):
    u = sorted(h[v], key = lambda x: s[x])
    G = []
    j = 0
    while j < len(u):
        e = j
        while e < len(u) and s[u[e]] == s[u[j]]:
            e += 1
        G.append(u[j:e])
        j = e
    P = 1
    R = []
    for w in G:
        x = C(g[s[w[0]]], len(w))
        R.append(x)
        P = min(W, P * x)
    z[v] = t // P + 1
    t = t % P
    for i in range(len(G)):
        o = U(g[s[G[i][0]]], len(G[i]), t % R[i])
        t = t // R[i]
        for j in range(len(G[i])):
            A(G[i][j], o[j])
A(1, 0)
print(a)
print(*z[1:])
