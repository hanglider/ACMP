n = int(input())
a = b = 1
for i in range(n // 2):
    a, b = 4 * a - b, a
print(a * (1 - n % 2))
