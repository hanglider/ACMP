d = list(map(int, open(0).read().split()))
n, m, r = d[:3]
k = max(n, m) + 1
x = [10**9] * k
y = [10**9] * k
p = [0] * k
q = [0] * k
for i in range(r):
    a, b, c = d[3 + 3 * i:6 + 3 * i]
    if c < x[a]:
        x[a] = c
        p[a] = i + 1
    if c < y[b]:
        y[b] = c
        q[b] = i + 1
w = [[0] * k for _ in range(k)]
e = [[0] * k for _ in range(k)]
for i in range(r):
    a, b, c = d[3 + 3 * i:6 + 3 * i]
    if x[a] + y[b] - c > w[a][b]:
        w[a][b] = x[a] + y[b] - c
        e[a][b] = i + 1
u = [0] * k
v = [0] * k
f = [0] * k
g = [0] * k
for i in range(1, k):
    f[0] = i
    j = 0
    t = [10**9] * k
    s = [0] * k
    while f[j]:
        s[j] = 1
        h = f[j]
        z = 10**9
        for l in range(1, k):
            if not s[l]:
                o = -w[h][l] - u[h] - v[l]
                if o < t[l]:
                    t[l] = o
                    g[l] = j
                if t[l] < z:
                    z = t[l]
                    b = l
        for l in range(k):
            if s[l]:
                u[f[l]] += z
                v[l] -= z
            else:
                t[l] -= z
        j = b
    while j:
        b = g[j]
        f[j] = f[b]
        j = b
a = set()
for j in range(1, k):
    i = f[j]
    if e[i][j]:
        a.add(e[i][j])
        x[i] = y[j] = 0
        p[i] = q[j] = 0
for i in range(1, n + 1):
    a.add(p[i])
for j in range(1, m + 1):
    a.add(q[j])
a.discard(0)
a = sorted(a)
print(sum(d[5 + 3 * i - 3] for i in a))
print(len(a))
print(*a)
