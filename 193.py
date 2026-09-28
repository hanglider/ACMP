n, m, k, *a = map(int, open(0).read().split())
b = [[m, n, 0, 0] for _ in range(k + 2)]
for i, v in enumerate(a):
    x = i % m
    y = n - i // m
    for j in {v, (k + 1) * (v > 0)}:
        b[j] = [min(b[j][0], x), min(b[j][1], y - 1), max(b[j][2], x + 1), max(b[j][3], y)]
for r in b[1:-1]:
    print(*[r, b[-1]][r[2] < 1])
