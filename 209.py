from math import gcd
n, *a = map(int, open(0).read().split())
x = a[::2]
y = a[1::2]
s = b = 0
for i in range(n):
    s += x[i - 1] * y[i] - x[i] * y[i - 1]
    b += gcd(x[i] - x[i - 1], y[i] - y[i - 1])
print((abs(s) - b + 2) // 2)
