n, m, *a = map(int, open(0).read().split())
p = [0, *range(n - 1, -1, -1)]
b = (1 << n) - 1
r = []
for x in a:
    r += (b >> p[x]).bit_count(),
    b ^= 1 << p[x] | 1 << n
    p[x] = n
    n += 1
print(*r)
