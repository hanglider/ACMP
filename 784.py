n, a, b = map(int, open(0).read().split())
while a - b:
    a, b = max(a, b) // 2, min(a, b)
print(a)
