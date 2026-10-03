n, *a = map(int, open(0).read().split())
d = [[0] * n for i in a]
for l in range(2, n):
    for i in range(n - l):
        j = i + l
        d[i][j] = min(d[i][k] + d[k][j] + a[k] * (a[i] + a[j]) for k in range(i + 1, j))
print(d[0][-1])
