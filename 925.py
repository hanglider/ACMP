t, n, a, b, c = map(int, open(0).read().split())
print([max(0, a + b + c - 2 * n), min(a, b, c)][t - 1])
