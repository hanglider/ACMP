n = int(input())
x = max(x for x in range(n) if x - -x // 100 * 7 <= n)
print(x, -x // 100 * -7)
