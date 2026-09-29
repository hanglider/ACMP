n = int(input())
k = n - 21
d = k % 8 + 2
print(n - 1 if n < 12 else [22, 30, 41, 50, 61, 70, 81, 90, 111][n - 12] if n < 21 else str(d) + '01'[d % 2] * (k // 8 + 2))
