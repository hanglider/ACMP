n, m = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]

a = [[0] * m for i in range(n)]
a[0][0] = 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            continue
        y = x[i][j]
        if y == 0:
            continue
        if i + y < n:
            a[i + y][j] += a[i][j]
        if j + y < m:
            a[i][j + y] += a[i][j]

print(a[n - 1][m - 1])