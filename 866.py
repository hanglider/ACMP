import sys
sys.setrecursionlimit(9999)
n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]
o = [1]
q = {1: 0}
p = [0] * (n + 1)
l = [1] * (n + 1)


def d(v):
    q[v] = len(o)
    o.append(v)
    l[v] = v
    for w in g[v]:
        if w not in q:
            p[w] = v
            d(w)
            if q[l[w]] < q[l[v]]:
                l[v] = l[w]
        elif q[w] < q[l[v]]:
            l[v] = w


t = g[1][0]
p[t] = 1
d(t)
r = [1, t]
s = {1: 0}
for v in o[2:]:
    x = p[v]
    i = r.index(x)
    if s[l[v]]:
        r.insert(i + 1, v)
        s[x] = 0
    else:
        r.insert(i, v)
        s[x] = 1
print(*r)
print(1, *r[:0:-1])
