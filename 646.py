n, k, *a = map(int, open(0).read().split())
m = (1 << 64 * k) - 1
p = 1
for x in a:
    p += p << 64 * min(x, k) & m
print((2**n - 2 * (p * (m // (2**64 - 1)) >> 64 * k - 64) % 2**64) * (sum(a) >= 2 * k))
