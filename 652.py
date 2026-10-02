from itertools import accumulate, chain
from bisect import bisect_left
from operator import sub
f = open(0)
n, k = map(int, f.readline().split())
q = [[1, n * n + n, n]]
t = [n]
u = [n * n + n]
for l in f:
    if len(q) > 250:
        z = [*chain(*q)]
        q = [z[i:i + 300] for i in range(0, len(z), 300)]
        u = [sum(b[1::3]) for b in q]
        t = [sum(map(abs, map(sub, b[2::3], b[::3]))) + len(b) // 3 for b in q]
    o, l, r = l.split()
    l = int(l)
    r = int(r)
    x = []
    for p in l - 1, r:
        c = [0, *accumulate(t)]
        i = bisect_left(c, p)
        if c[i] > p:
            i -= 1
            v = p - c[i]
            h = v
            z = q[i]
            j = 0
            while h:
                g = abs(z[j + 2] - z[j]) + 1
                if g > h:
                    a = z[j]
                    d = (z[j + 2] > a) * 2 - 1
                    e = a + d * h
                    y = (a + e - d) * h
                    z[j + 1:j + 2] = [y, e - d, e, z[j + 1] - y]
                    h = g
                h -= g
                j += 3
            y = sum(z[1:j:3])
            q[i:i + 1] = [z[:j], z[j:]]
            t[i:i + 1] = [v, t[i] - v]
            u[i:i + 1] = [y, u[i] - y]
            i += 1
        x += [i]
    a, b = x
    if o > "R":
        print(sum(u[a:b]) // 2)
    else:
        q[a:b] = q[a:b][::-1]
        t[a:b] = t[a:b][::-1]
        u[a:b] = u[a:b][::-1]
        for z in q[a:b]:
            z.reverse()
