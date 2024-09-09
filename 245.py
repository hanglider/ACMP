n = int(input())
a = sorted([int(input()) for i in range(n)])
p = [0]*(n+1)
p[0] = 0
for i in range(0,n):
    p[i+1] = p[i] + a[i]
if n <= 2: print(sum(a))
else:
    i = 0
    j = 1
    r = p[1]
    while j < n:
        if a[j] <= a[i] + a[i+1]: j += 1
        else: i += 1
        r = max(r, p[j] - p[i])
    print(r)