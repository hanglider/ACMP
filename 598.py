from itertools import*
n = int(input())
a = [input().split() for _ in range(n)]
g = max((c for k in range(1, 6) for c in combinations(range(n), k) if all(a[i][j] > '0' for i, j in combinations(c, 2))), key=len)
v = 1
print(n - len(g) + 1)
print(*[1 if i in g else (v := v + 1) for i in range(n)])
