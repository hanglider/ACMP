n, k = map(int, input().split())
r = []
for h in k - 1, k:
    d = [1] + [0] * h
    for _ in range(2 * n):
        d = [x + y for x, y in zip([0] + d, d[1:] + [0])]
    r += [d[0]]
print(r[1] - r[0])
