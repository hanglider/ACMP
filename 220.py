import bisect, collections
*p, s = open(0).read().split(None, 5)
u, h, t, l, n = map(int, p)
k = max(0, (l - 1 - u + t) // t)
c = collections.Counter()
d = [0] * (u + t)
while s:
    q = s.split(None, 4**7)
    s = ''.join(q[4**7:])
    q = list(map(int, q[:4**7]))
    i = bisect.bisect(q, u - 2)
    j = max(i, bisect.bisect(q, k * t))
    c.update(map(t.__rmod__, q[i:j]))
    for v in q[:i] + q[j:]:
        a = v - min(k, v // t) * t
        b = v - max(0, (v - u + t) // t) * t
        if a <= b:
            d[a] += 1
            d[b + t] -= 1
for r, m in c.items():
    d[r] += m
    d[u - 1 - (u - 1 - r) % t + t] -= m
for i in range(t, u + t):
    d[i] += d[i - t]
s = sum(d[:h])
m = s
for i in range(h, u):
    s += d[i] - d[i - h]
    m = min(m, s)
print(m)
