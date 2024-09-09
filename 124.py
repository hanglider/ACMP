n,m = map(int, input().split())
a = [0]*n 
for i in range(m):
    l, r = map(int, input().split())
    a[l-1] += 1
    a[r-1] += 1
for i in a:
    print(i, end=' ')