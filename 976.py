n = int(open('input.txt').read())
f = lambda m, p, s, k: sum((p * x - s - x == n - k - 1) + f(x, p * x, s + x, k + 1) for x in range(m, 2 * n // p + 1))
print(f(2, 1, 0, 0))