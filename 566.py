a, b, c, k = map(int, input().split())
q = -(-k // 3)
z = (k - 1) // 3
p = k % 2
g = z - (z + p) % 2
e = z - (z + p + 1) % 2
def f(t):
    for i in range(min(t, c // q) + 1):
        m = t - i
        for o in range(m + 1):
            l = o * (1 - p) + (m - o) * p
            s = min(c - i * q, o * e + (m - o) * g)
            s -= (s - l) % 2
            r = m * k - 3 * s
            if s >= l and a + b + min(b, (r - o) // 2) >= r:
                return 1
l = 0
r = (a + 2 * b + 3 * c) // k
while l < r:
    m = (l + r + 1) // 2
    if f(m):
        l = m
    else:
        r = m - 1
print(l)
