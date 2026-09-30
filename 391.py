x, m, l, v = map(int, input().split())
print(next(s for s in map('{:04}'.format, range(10**4)) if sum(int(c) * x**i for i, c in enumerate(s)) % m == v).ljust(l, '0'))
