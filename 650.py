from collections import Counter
n, m, *e = map(int, open(0).read().split())
p = [*range(n + 1)]
def f(x):
    while p[x] - x:
        p[x] = x = p[p[x]]
    return x
for x, y in zip(e[::2], e[1::2]):
    p[f(x)] = f(y)
v = Counter(map(f, range(1, n + 1)))
w = Counter(map(f, e[::2]))
print(sum(k * (k * k // 4 - k + 1) if w[r] == k else k * (k - 1) * (k - 2) // 3 for r, k in v.items()))
