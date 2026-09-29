s = input()
a, b, c, d = map(ord, s[:2] + s[4:6])
k = lambda x, y, u, v: abs((x - u) * (y - v)) == 2
print(1 if k(a, b, c, d) else 2 if any(k(a, b, i, j) and k(i, j, c, d) for i in range(97, 105) for j in range(49, 57)) else "NO")
