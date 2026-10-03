n, m, *a = map(int, open(0).read().split())
p = []
for j in range(m):
    x = (1 << (1 << j)) - 1 << (1 << j)
    for t in range(j + 1, m):
        x |= x << (1 << t)
    p += [x]
g = (1 << (1 << m)) - 1
for i in range(n):
    b = 0
    for j in range(m):
        if a[i * m + j] < 1:
            b |= p[j]
    g &= b
c = [1] + [0] * m
for t in range(m):
    c = [1] + [c[k] | c[k - 1] << (1 << t) for k in range(1, m + 1)]
for k in range(m + 1):
    h = g & c[k]
    if h:
        s = h.bit_length() - 1
        print(k)
        print(*[j + 1 for j in range(m) if s >> j & 1])
        exit()
print("Impossible")
