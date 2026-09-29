n, *s = open(0).read().split()
n = int(n)
d = [[10**9] * (n + 1) for _ in range(n + 1)]
d[n][n - 1] = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        d[i][j] = int(s[i][j]) + min(d[i + 1][j], d[i][j + 1])
r = [["."] * n for _ in s]
i = j = 0
while i < n:
    r[i][j] = "#"
    if d[i + 1][j] < d[i][j + 1]:
        i += 1
    else:
        j += 1
for x in r:
    print(*x, sep="")
