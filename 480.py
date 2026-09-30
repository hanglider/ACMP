n, *a, k = map(int, open(0).read().split())
s = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    s[i] = s[i + 1] + a[i]
f = [[0] * (n + k + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for j in range(1, n + k + 1):
        f[i][j] = max(f[i][j - 1], s[i] - f[min(i + j, n)][j])
print(f[0][k])
