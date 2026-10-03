n, *a = map(int, open(0).read().split())
print(["NO", "YES"][max(a[::2]) <= min(a[1::2])])
