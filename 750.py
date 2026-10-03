import sys
sys.setrecursionlimit(9999)
n, m, k, *e = map(int, open(0).read().split())
a = [0] * n
b = [0] * m
for x, y in zip(e[::2], e[1::2]):
    a[x - 1] |= 1 << y - 1
    b[y - 1] |= 1 << x - 1
r = [-1] * m
l = [-1] * n


def K(u):
    global v
    c = a[u] & ~v
    while c:
        w = c & -c
        i = w.bit_length() - 1
        v |= w
        if r[i] < 0 or K(r[i]):
            r[i] = u
            l[u] = i
            return 1
        c = a[u] & ~v
    return 0


for u in range(n):
    v = 0
    K(u)


def F(a, t, s):
    q = [i for i in range(len(s)) if s[i] < 0]
    z = set(q)
    o = 0
    while q:
        c = a[q.pop()] & ~o
        o |= c
        while c:
            x = t[(c & -c).bit_length() - 1]
            c &= c - 1
            if x not in z:
                z.add(x)
                q += [x]
    print(''.join('NP'[i in z] for i in range(len(s))))


F(a, r, l)
F(b, l, r)
