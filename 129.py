n, m, *a = map(int, open(0).read().split())
k = n * m
d = [(1 - x) * k for x in a]
for s in 1, -1:
    for i in range(k)[::s]:
        for j in i - s, i - s * m:
            if 0 <= j < k and (j // m == i // m or j % m == i % m):
                d[i] = min(d[i], d[j] + 1)
for i in range(n):
    print(*d[i * m:i * m + m])
