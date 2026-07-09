v = open('input.txt').read().split()
n = int(v[0])
m = int(v[1])
k = int(v[2])
g = [int(x) for x in v[3:3 + n * m]]
q = 3 + n * m
S = {1: 1, 2: 2, 3: 3, 4: 3}
B = {1: [(0, 0)], 2: [(0, 0), (0, 1)], 3: [(0, 0), (0, 1), (0, 2)], 4: [(0, 0), (0, 1), (1, 1)]}
T = []
for _ in range(k):
    f = int(v[q])
    w = int(v[q + 1])
    s = S[f]
    c = [int(x) for x in v[q + 2:q + 2 + s]]
    q += 2 + s
    p = list(zip(B[f], c))
    e = set()
    for _ in range(4):
        p = [((b, -a), x) for (a, b), x in p]
        a, b = min(y for y, x in p)
        e.add(tuple(sorted((((y - a, z - b), x) for (y, z), x in p))))
    for o in e:
        T.append((w, o))
P = [[] for _ in range(n * m)]
for i in range(n):
    for j in range(m):
        for w, o in T:
            b = 0
            for (y, z), x in o:
                y += i
                z += j
                if y < n and 0 <= z < m and g[y * m + z] == x:
                    b |= 1 << ((y - i) * m + z - j)
                else:
                    b = -1
                    break
            if b > 0:
                P[i * m + j].append((b, w))
D = {0: 0}
for i in range(n * m):
    E = {}
    for u, c in D.items():
        if u & 1 or g[i] == 2:
            h = u >> 1
            if c < E.get(h, 9**9):
                E[h] = c
        else:
            for b, w in P[i]:
                if u & b == 0:
                    h = (u | b) >> 1
                    t = c + w
                    if t < E.get(h, 9**9):
                        E[h] = t
    D = E
print(D.get(0, -1))
