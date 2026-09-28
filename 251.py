n, m, *a = map(int, open(0).read().split())
b = a[n:]
a = a[:n]
for l in b[::-1]:
    q = min(a)
    r = [a[(l - 1 - i) % n] for i in range(n)].index(q)
    a = [x - q for x in a]
    for i in range(r):
        a[(l - 1 - i) % n] -= 1
    a[(l - 1 - r) % n] = q * n + r
print(*a)
