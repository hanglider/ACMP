n, *a = map(int, open(0).read().split())
d = [[0] * n for _ in a]
for l in range(1, n):
    for i in range(n - l):
        j = i + l
        d[i][j] = a[2 * i] * a[2 * j + 1] + min(d[i][s] + d[s + 1][j] for s in range(i, j))
print(d[0][n - 1])
