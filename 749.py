n = int(input())
k = max((j for j in range(2, 61) for r in [round(n ** (1 / j))] if any((r + i)**j == n for i in (-1, 0, 1))), default=1)
t = k + 1
d = [1] + [0] * (t * t - 1)
for a in range(t):
    for b in range(t):
        if a + b:
            for x in range(a, t):
                for y in range(b, t):
                    d[x * t + y] += d[(x - a) * t + y - b]
print(d[-1] - 1)
