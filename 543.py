n, w, d, p = map(int, open(0).read().split())
print((w * n * (n - 1) // 2 - p) // d or n)
