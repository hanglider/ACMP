import random
n, m, *r = open(0).read().split()
n = int(n)
m = int(m)
x, y = divmod(''.join(r).index('K'), m)
W = m + 4
L = W * (n + 4)
h = [0] * L
for i in range(n):
    h[(i + 2) * W + 2:(i + 3) * W - 2] = [1] * m
D = [-2 * W - 1, -2 * W + 1, -W - 2, -W + 2, W - 2, W + 2, 2 * W - 1, 2 * W + 1]
g = [sum(h[(i + d) % L] for d in D) for i in range(L)]
s = []
while len(s) < n * m:
    for q in s:
        h[q] = 1
        for d in D:
            g[q + d] += 1
    c = [random.random() * (n + m) - (i // W - 2 - (n - 1) / 2) ** 2 - (i % W - 2 - (m - 1) / 2) ** 2 for i in range(L)]
    s = []
    t = [[(0, 0, (x + 2) * W + y + 2)]]
    z = 0
    while len(s) < n * m and z < 2 * n * m:
        z += 1
        if t[-1]:
            q = t[-1].pop()[2]
            h[q] = 0
            for d in D:
                g[q + d] -= 1
            s += [q]
            t += [sorted([(g[q + d], c[q + d], q + d) for d in D if h[q + d]], reverse=True)]
        else:
            q = s.pop()
            t.pop()
            h[q] = 1
            for d in D:
                g[q + d] += 1
o = [0] * L
for k, q in enumerate(s):
    o[q] = k + 1
for i in range(n):
    print(*o[(i + 2) * W + 2:(i + 3) * W - 2])
