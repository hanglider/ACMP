n, k = map(int, open(0).read().split())
d = [0, 1] + [0] * k
for _ in range(n - 1):
    d = [0] + [d[i] * i + d[i - 1] for i in range(1, k + 1)]
print(sum(d))
