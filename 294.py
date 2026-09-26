a, b, c, d, e, f = map(int, open('input.txt').read().split())
p = min(a * (100 - b), d * (100 - e)) // 100
print((a - p) * c + (d - p) * f)