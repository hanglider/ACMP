from math import comb as C
m, n, w, b = map(int, input().split())
print(sum(C(m, r) * C(n, c) * C((m - r) * (n - c), b) * C(r, i) * C(c, j) * C(i * j, w) * (-1)**(r + c - i - j) for r in range(m + 1) for c in range(n + 1) for i in range(r + 1) for j in range(c + 1)))
