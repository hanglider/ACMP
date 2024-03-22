k,n = map(int, input().split())
a = []
for i in range(k*n+1): a.append(0)
a[0] = 1
for i in range(n):
    for j in range(1, k + 1):
        a[i + j] += a[i]
print(a[n])