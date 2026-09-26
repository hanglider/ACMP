from array import *
from itertools import accumulate
I = open('input.txt').readline
n = int(I())
K = 46656
U = array('i')
V = array('i')
for _ in range(n):
    s = I().strip()
    U.append(int(s[:3], 36))
    V.append(int(s[-3:], 36))
o = array('i', [0]) * K
for u in U:
    o[u] += 1
o = array('i', accumulate(o))
f = o[:]
w = V[:]
for u, v in zip(U, V):
    f[u] -= 1
    w[f[u]] = v
x = array('i', [0]) * K
l = x[:]
C = array('i', [-1]) * K
S = []
c = m = 0
for r in U:
    if x[r]:
        continue
    c += 1
    x[r] = l[r] = c
    S.append(r)
    t = [r]
    while t:
        a = t[-1]
        if f[a] < o[a]:
            b = w[f[a]]
            f[a] += 1
            if not x[b]:
                c += 1
                x[b] = l[b] = c
                S.append(b)
                t.append(b)
            elif C[b] < 0:
                l[a] = min(l[a], x[b])
        else:
            t.pop()
            if t:
                l[t[-1]] = min(l[t[-1]], l[a])
            if l[a] == x[a]:
                b = -1
                while b != a:
                    b = S.pop()
                    C[b] = m
                m += 1
A = [0] * m
B = [0] * m
for u, v in zip(U, V):
    if C[u] != C[v]:
        A[C[u]] = B[C[v]] = 1
print((m > 1 < n) * max(A.count(0), B.count(0)))
