n, *a = map(int, open(0).read().split())
s = {*zip(a[::2], a[1::2])}
print(4 * n - 2 * sum(((x + 1, y) in s) + ((x, y + 1) in s) for x, y in s))
