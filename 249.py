s = open(0).read().strip()
n = len(s)
d = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n + 1):
        d[i][j] = min([d[i + 1][j] + 1] + [d[i + 1][k] + d[k + 1][j] for k in range(i + 1, j) if s[i] + s[k] in '() [] {}'])
print(d[0][n])
