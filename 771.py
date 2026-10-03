n, *a = open(0).read().split()
c = {}
for v, p in sorted(zip(a[::2], a[1::2])):
    c.setdefault(p, []).append(v)
o = {}
r = [[' '] * 300 for _ in range(300)]


def f(v):
    a = []
    for k in c.get(v, []):
        b = f(k)
        o[k] = max(a[:len(b)], default=-2) + 2
        a[:len(b)] = [o[k] + x for x in b]
    return [0] + a


def g(v, x, d):
    s = c.get(v, [])
    if s and d >= 0:
        r[2 * d + 1][x] = '|'
    z = x
    for k in s:
        y = x + o[k]
        r[2 * d + 2][z:y] = '-' * (y - z)
        r[2 * d + 2][y] = k
        g(k, y, d + 1)
        z = y + 1


f('-')
g('-', 0, -1)
for l in r:
    l = ''.join(l).rstrip()
    if l:
        print(l)
