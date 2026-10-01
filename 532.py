from heapq import *
from array import array
n, m, p = map(int, input().split())
k = array('q')
z = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    z += b * (d - c)
    if a > b:
        k.append((a - b << 34) + (c << 17) + d)
k = array('q', sorted(k))
n = len(k)
w = array('i', (x >> 34 for x in k))
c = array('i', [-1]) * (p + 1)
d = array('i', [-1]) * (p + 1)
e = array('i', [0]) * n
f = array('i', [0]) * n
for x in range(n):
    e[x] = c[k[x] >> 17 & 131071]
    c[k[x] >> 17 & 131071] = x
    f[x] = d[k[x] & 131071]
    d[k[x] & 131071] = x
k = list(range(n))
s = bytearray(n)
t = []
r = []
u = q = l = 0
for y in range(1, p):
    x = d[y]
    while x >= 0:
        if s[x] > 1:
            l -= 1
        else:
            u -= w[x]
            q -= 1
            if l:
                v = k[~heappop(r)]
                while s[v] < 2:
                    v = k[~heappop(r)]
                heappush(t, v)
                s[v] = 1
                u += w[v]
                q += 1
                l -= 1
        s[x] = 0
        x = f[x]
    x = c[y]
    while x >= 0:
        x = k[x]
        heappush(t, x)
        s[x] = 1
        u += w[x]
        q += 1
        if q > m:
            v = heappop(t)
            while s[v] < 1:
                v = heappop(t)
            heappush(r, k[~v])
            s[v] = 2
            u -= w[v]
            q -= 1
            l += 1
        x = e[x]
    z += u
print(z)
