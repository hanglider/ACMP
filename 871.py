n, m, *a = map(int, open(0).read().split())
print('YES' if len({frozenset(p) for p in zip(a[::2], a[1::2])}) >= n else 'NO')
