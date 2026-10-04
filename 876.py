a, b, r = map(float, input().split())
h = (a * a + b * b)**.5
print(r * h)
print(a * r / h, b * r / h)
