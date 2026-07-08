n = int(input())
a = list(map(int, input().split()))
b = 1
d = 0
m = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        nd = 1
    elif a[i] < a[i - 1]:
        nd = -1
    else:
        nd = 0
    if nd == 0:
        b = 1
    elif d == 0 or nd != d:
        b += 1
    else:
        b = 2
    d = nd
    if b > m:
        m = b
print(m)
