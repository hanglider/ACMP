_, *a = map(int, open(0).read().split())
for n, m in zip(a[::2], a[1::2]):
    print(["No", "Yes"][n > 1 and 2 * m <= (n - 1) * (n - 2)])
