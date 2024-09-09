n = int(input())
m = n
#n, m = [int(i) for i in input().split()]
spiral = [[0] * m for _ in range(n)]
c = 1
for k in range(min(n // 2 + 1, m //2 + 1)):  
    for j in range(k, m - k):  
        if spiral[k][j] == 0:  
            spiral[k][j] = c 
            c += 1
    for i in range(1 + k, n - k):  
        if spiral[i][m - k - 1] == 0:
            spiral[i][m - k - 1] = c 
            c += 1
    for j in range(m - k - 2, k - 1, -1):  
        if spiral[n - k - 1][j] == 0:
            spiral[n - k - 1][j] = c 
            c += 1
    for i in range(n - k - 2, k, -1):  
        if spiral[i][k] == 0:
            spiral[i][k] = c 
            c += 1
for i in range(n):  
    for j in range(m):
        print(str(spiral[i][j]).ljust(3), end=' ')
    print()