n, m, r, *a = map(int, open(0).read().split())
c = m + 2 * n
f = (1 << 40 * c) - 1
o = f // ((1 << 40) - 1)
k = (1 << 40 * (m + n)) - (1 << 40 * n)
g = 4 * r * o
q = 15 * o
b = (1 << 36) // r
v = sum(x % r << 40 * (n + i) for i, x in enumerate(a))
u = v
w = 0
for _ in range(n - 1):
    s = (u << 40) + (u >> 40) + v + g - w
    s = s - (s * b >> 36 & q) * r & f
    w = u
    v = s & k
    u = s + v
print(*[(v >> 40 * (n + i) & 2**40 - 1) % r for i in range(m)])
