n, *a = map(int, open(0).read().split())
d = [0] + [-9**9] * n
for j in range(n):
    d = [max([d[s]] + [d[s - i - 1] + a[i * n + j] for i in range(s)]) for s in range(n + 1)]
print(d[n])
