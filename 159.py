n, *a = map(int, open(0).read().split())
print(*[i for _, i in sorted(zip(a, range(1, n + 1)))])
