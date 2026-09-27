n, k = map(int, input().split())
d = [0] * 80
d[n] = 1
for _ in range(k - 1):
    d = [0] + [x + y for x, y in zip(d, d[2:])] + [0]
print(d[1])
