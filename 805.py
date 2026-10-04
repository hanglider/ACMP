n, *a = map(int, open(0).read().split())
d = max(0, min(map(sum, zip(a[::3], a[1::3], a[2::3]))) - max(a[::3]) - max(a[1::3]))
print('%.3f' % (d * d / 2))
