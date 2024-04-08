n, m = map(int, input().split())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                a[i][j] = a[i][j]
            else: a[i][j] += a[i][j-1]
        elif j != 0: a[i][j] += min(a[i-1][j], a[i][j-1])
        else: a[i][j] += a[i-1][j] 
print(a[n-1][m-1])