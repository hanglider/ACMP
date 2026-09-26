n, m, d, k = map(int, open('input.txt').read().split())
print(d * ((n + m) * k - n * m * d))