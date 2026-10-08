n = int(input())
d = [1] * (n + 1)
for p in range(2, n + 1):
    if all(p % i for i in range(2, p)):
        for s in range(n, 1, -1):
            q = p
            while q <= s:
                d[s] = max(d[s], d[s - q] * q)
                q *= p
print(d[n])
