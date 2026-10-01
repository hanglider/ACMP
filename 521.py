p, k = map(int, input().split())
s = 0
for n in range(p, k + 1):
    while n > 2:
        n = [n // 2, 3 * n + 1][n % 2]
        s += 1
print(s)
