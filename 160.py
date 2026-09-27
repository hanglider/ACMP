from math import lcm
n, *a = map(int, open(0).read().split())
r = 1
for i in range(n):
    j = a[i]
    k = 1
    while j != i + 1:
        j = a[j - 1]
        k += 1
    r = lcm(r, k)
print(r)
