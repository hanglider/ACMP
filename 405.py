import sys
from array import array
I = sys.stdin.buffer.readline
n, m = map(int, I().split())
U = array('i', [0]) * m
V = U[:]
o = array('i', [0]) * (n + 2)
for i in range(m):
    a, b = map(int, I().split())
    U[i] = a
    V[i] = b
    o[a] += 1
    o[b] += 1
for i in range(1, n + 2):
    o[i] += o[i - 1]
f = o[:]
E = array('i', [0]) * (2 * m)
W = E[:]
for i in range(m):
    for a, b in (U[i], V[i]), (V[i], U[i]):
        f[a] -= 1
        E[f[a]] = b
        W[f[a]] = i
t = array('i', [0]) * (n + 1)
l = t[:]
z = t[:]
A = t[:]
e = t[:]
B = array('q', [0]) * (n + 1)
t[1] = l[1] = z[1] = c = 1
e[1] = -1
s = [1]
while s:
    v = s[-1]
    if f[v] < o[v]:
        j = f[v]
        f[v] += 1
        if W[j] != e[v]:
            u = E[j]
            if t[u]:
                l[v] = min(l[v], t[u])
            else:
                c += 1
                t[u] = l[u] = c
                e[u] = W[j]
                z[u] = 1
                s.append(u)
    else:
        s.pop()
        if s:
            w = s[-1]
            l[w] = min(l[w], l[v])
            z[w] += z[v]
            if l[v] >= t[w]:
                A[w] += z[v]
                B[w] += z[v] * z[v]
print('\n'.join(str(n - 1 + ((n - 1)**2 - B[v] - (n - 1 - A[v])**2) // 2) for v in range(1, n + 1)))