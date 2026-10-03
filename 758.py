n, *a = map(int, open(0).read().split())
a.sort()
s = 0
while n > 3:
    s += a[n - 1] + a[0] + min(2 * a[1], a[0] + a[n - 2])
    n -= 2
print(s + a[n - 1] + (n > 2) * sum(a[:2]))
