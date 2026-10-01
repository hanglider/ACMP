from math import gcd
r = open(0).read().split()
n, m, k = map(int, r[:3])
a = sorted(map(int, r[3:]))
e = [[gcd(p, q) >= k for q in a] for p in a]
d = [(w, 1 << w, 48 * w, sum(e[w][v] << 48 * v for v in range(n) if v != w)) for w in range(n)]
s = [0] * (1 << n)
for w, b, h, c in d:
    s[b] = c
for t in range(1, 1 << n):
    if t & t - 1:
        s[t] = sum((s[t ^ b] >> h & 2**48 - 1) * c for w, b, h, c in d if t & b)
t = (1 << n) - 1
p = []
while t:
    for w, b, h, c in d:
        if t & b and (not p or e[p[-1]][w]):
            x = s[t ^ b] >> h & 2**48 - 1 if t ^ b else 1
            if m <= x:
                break
            m -= x
    else:
        print(-1)
        exit()
    p += w,
    t ^= b
print(*[a[i] for i in p])
