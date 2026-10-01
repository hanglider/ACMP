n = int(input())
b = n // 144
print(*min((2280 * i + 205 * j + 21 * (k := max(0, n - 144 * i - 12 * j)), i, j, k) for i in range(b, b + 2) for j in range(13))[1:])
