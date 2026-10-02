from heapq import *
from array import array
from itertools import *
def z():
    a = open(0, 'rb').read()
    q = [0]
    while q[-1] < len(a):
        q += [a.find(b' ', q[-1] + 65536) % (len(a) + 1)]
    g = map(int, chain.from_iterable(a[i:j].split() for i, j in zip(q, q[1:])))
    m = next(g)
    L = array('i')
    R = array('i')
    s = array('i', [0])
    for c in range(m):
        t = array('i', islice(g, 2 * next(g)))
        L.extend(t[::2])
        R.extend(t[1::2])
        s.append(len(L))
    n = len(L)
    p = array('i', range(n))
    for c in range(m - 1):
        i, a, b = s[c:c + 3]
        j = a
        while i < a <= j < b:
            if L[i] <= R[j] and L[j] <= R[i]:
                x = i
                while p[x] != x:
                    p[x] = x = p[p[x]]
                y = j
                while p[y] != y:
                    p[y] = y = p[p[y]]
                p[x] = y
            if R[i] < R[j]:
                i += 1
            else:
                j += 1
    for i in range(n):
        x = i
        while p[x] != x:
            p[x] = x = p[p[x]]
        p[i] = x
    r = p
    d = array('i', [10**7]) * n
    x = array('i', [-1]) * n
    y = array('i', [-1]) * n
    for i in range(n):
        k = r[i]
        x[i] = y[k]
        y[k] = i
        if L[i] <= d[k]:
            d[k] = L[i] - 1
    h = [d[i] << 17 | i for i in range(n) if r[i] == i]
    heapify(h)
    e = set(s)
    while h:
        t = heappop(h)
        v = t >> 17
        k = t & 131071
        if v > d[k]:
            continue
        i = y[k]
        while i >= 0:
            if i + 1 not in e:
                k = r[i + 1]
                w = v + L[i + 1] - R[i] - 1
                if w < d[k]:
                    d[k] = w
                    heappush(h, w << 17 | k)
            i = x[i]
    print(*[s[c + 1] > s[c] and R[s[c + 1] - 1] - d[r[s[c + 1] - 1]] or 0 for c in range(m)])
z()
