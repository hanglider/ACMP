x, y = map(int, input().split())
x += 1
y += 1
a = 0
for i in range(30):
    b = 1 << i
    c = b * 2
    d = x // c * b + max(0, x % c - b)
    e = y // c * b + max(0, y % c - b)
    a += (d * (y - e) + (x - d) * e) * b
print(a)