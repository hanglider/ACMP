n, *a = map(int, open(0).read().split())
k = a.index(max(a))
c = max([x for x, y in zip(a[k + 1:], a[k + 2:]) if x % 10 == 5 and y < x] or [0])
print(c and sum(x > c for x in a) + 1)
