n, m = map(int, input().split())
if m == 1:
    print(n)
    exit()
if m == 0:
    print(1)
    exit()
c = 0
p = m
while m <= n:
    c += n-m+1
    m += p-1
print(c)