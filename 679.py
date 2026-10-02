n = int(input())
a = -n % 3
b = (n - 2 * a) // 3
print(*[2, a] * (a > 0), *[3, b] * (b > 0))
