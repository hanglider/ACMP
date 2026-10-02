n, k, m, *e = map(int, open(0).read().split())
a = [0] * n
for i in range(m):
    x = e[2 * i] - 1
    y = e[2 * i + 1] - 1
    a[x] |= 1 << y
    a[y] |= 1 << x
h = n // 2
r = n - h
t = sorted(range(1 << r), key=int.bit_count)
c = [0]
for i in range(r + 1):
    c += [c[-1] + [x.bit_count() for x in t].count(i)]
v = 0
p = [0] * h
for j, x in enumerate(t):
    v += sum((a[h + i] >> h & x).bit_count() - a[h + i].bit_count() for i in range(r) if x >> i & 1) + 300 << 16 * j
    for i in range(h):
        p[i] += 2 * (a[i] >> h & x).bit_count() << 16 * j
b = -9**9
for g in range(1 << h):
    s = g ^ g >> 1
    if g:
        i = (g & -g).bit_length() - 1
        v += p[i] if s >> i & 1 else -p[i]
    j = k - s.bit_count()
    if 0 <= j <= r:
        w = memoryview(v.to_bytes(2 << r, 'little')).cast('H')[c[j]:c[j + 1]].tolist()
        z = max(w) + sum((a[i] & s).bit_count() - a[i].bit_count() for i in range(h) if s >> i & 1)
        if z > b:
            b = z
            u = s + (t[c[j] + w.index(max(w))] << h)
print(*[i + 1 for i in range(n) if u >> i & 1])
