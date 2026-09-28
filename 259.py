from array import *
from operator import *
s = open(0).read().split()[1]
n = len(s)
t = s + "#" + s[::-1] + "$"
e = 2 * n + 1
z = array("i", [0]) * e
l = r = 0
i = 1
g = 64
while i < e:
    if i < r - 30:
        w = min(r - i, g)
        c = z[i - l:min(i, i - l + w)]
        a = (c * (w // len(c) + 1))[:w]
        b = range(r - i, r - i - w, -1)
        p = -1
        if r != n and r != e:
            p = bytes(map(eq, a, b)).find(1)
        if p < 0:
            z[i:i + w] = array("i", map(min, a, b))
            i += w
            g *= 2
            continue
        z[i:i + p] = array("i", map(min, a[:p], b[:p]))
        i += p
        k = r - i
        g = 64
    elif i < r:
        k = r - i
        if z[i - l] != k:
            z[i] = min(z[i - l], k)
            i += 1
            continue
    else:
        i = t.find(s[0], i)
        if i < 0:
            break
        k = 0
    while t[k] == t[i + k]:
        k += 1
    z[i] = k
    l = i
    r = i + k
    i += 1
z = z[:n:-1]
for i in range(0, n, 9999):
    print(" ".join(map(str, z[i:i + 9999])), end=" ")
