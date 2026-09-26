a, b = map(int, open('input.txt').read().split())
s = round((a * b)**.5)
print(s * (s * s == a * b))