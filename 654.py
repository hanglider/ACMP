n, *a = map(int, open(0).read().split())
print(max(a) - sum(a) + sum(map(max, a, a[1:])))
