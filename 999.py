from array import *
I = open('input.txt').readline
n, m = map(int, I().split())
g = [[] for _ in range(n + 1)]
A = array('i')
for _ in range(m):
    u, v, t = map(int, I().split())
    if t:
        g[u].append(v)
        g[v].append(u)
    else:
        A.extend((u, v))
d = [-1] * (n + 1)
d[1] = 0
p = [0] * (n + 1)
q = [1]
for u in q:
    for v in g[u]:
        if d[v] < 0:
            d[v] = d[u] + 1
            p[v] = u
            q.append(v)
c = [0] * (n + 1)
for u, v in zip(A[::2], A[1::2]):
    if d[u] > d[v]:
        u, v = v, u
    c[u] -= 1
    c[v] += 1
r = 0
for v in q[:0:-1]:
    r += c[v] == 1
    c[p[v]] += c[v]
print(r)
