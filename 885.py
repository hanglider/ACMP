from collections import deque
n = int(input())
m = 2 * n + 1
g = [input() for _ in range(m)]
I = E = 0
for y in range(m):
    for x in range(m):
        if g[y][x] == 'O':
            I |= 1 << y * m + x
        if g[y][x] == 't':
            E |= 1 << y * m + x
S = lambda a, b: (a > b) - (a < b)
V = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if a or b]
s = (n * m + n, (1, 0), E, 0)
P = {s: None}
q = deque([s])
r = None if E else s
while q and not r:
    u = q.popleft()
    p, d, E, D = u
    x, y = p % m, p // m
    for k in range(9):
        e, f = E, D
        if k == 8:
            c = d
            o = p
            for a, b in ((-d[1], d[0]), (d[1], -d[0])):
                for j in range(1, 4):
                    i, h = x + a * j, y + b * j
                    if not (0 <= i < m and 0 <= h < m):
                        break
                    z = 1 << h * m + i
                    if z & I:
                        break
                    if z & e:
                        e ^= z
                        f |= z
                        break
            if not e:
                r = (o, c, e, f)
                P[r] = u
                break
        else:
            c = V[k]
            i, h = x + c[0], y + c[1]
            if not (0 <= i < m and 0 <= h < m):
                continue
            o = h * m + i
            if (1 << o) & (I | e | f):
                continue
        i, h = o % m, o // m
        w = {}
        t = e
        l = 0
        while t:
            b = t & -t
            t ^= b
            j = b.bit_length() - 1
            a = (j % m + S(i, j % m)) + (j // m + S(h, j // m)) * m
            if a == o:
                l = 1
                break
            if (1 << a) & (I | f):
                continue
            w[a] = w.get(a, 0) + 1
        if l:
            continue
        e = 0
        for a in w:
            if w[a] > 1:
                f |= 1 << a
            else:
                e |= 1 << a
        v = (o, c, e, f)
        if v not in P:
            P[v] = u
            q.append(v)
            if not e:
                r = v
                break
if r:
    z = []
    while P[r]:
        z.append('%d %d' % (r[0] % m, r[0] // m))
        r = P[r]
    print(len(z))
    print('\n'.join(z[::-1]))
else:
    print('IMPOSSIBLE')
