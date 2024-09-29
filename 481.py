s = input()
n = len(s)
a = [[1]*n]
a += [[0]*n for i in range(n-1)]
for i in range(1, n):
    for j in range(n):
        if j+i < n and s[j] == s[j+i]:
            a[i][j] = a[i - 1][j] + 1
            for k in range(j+1, j+i):
                a[i][j] += a[i - k + j - 1][k]
        else:
            a[i][j] = a[i - 1][j]
 
print(sum(a[n-1]))