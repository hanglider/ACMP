n, *a = map(int, open(0).read().split())
a.sort()
print(*a[::2] + a[1::2][::-1])
