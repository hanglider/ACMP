d = list(map(int, open(0).read().split()))
n = d[0]
k = d[1]
c = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
f = [[0] * (k + 1) for i in range(n + 1)]
f[0][0] = 1
for i in range(1, n + 1):
    for j in range(k + 1):
        for x in c:
            if j >= x and f[i - 1][j - x]:
                f[i][j] = 1
                break
if not f[n][k]:
    print("NO SOLUTION")
else:
    a = ""
    r = k
    for i in range(n):
        for v in range(10):
            if (v or i or n == 1) and r >= c[v] and f[n - 1 - i][r - c[v]]:
                a += str(v)
                r -= c[v]
                break
    b = ""
    r = k
    for i in range(n):
        for v in range(9, -1, -1):
            if (v or i or n == 1) and r >= c[v] and f[n - 1 - i][r - c[v]]:
                b += str(v)
                r -= c[v]
                break
    print(a)
    print(b)
