n, m, *a = map(int, open(0).read().split())
print(sum(sorted(a + [0] * m)[n:]))
