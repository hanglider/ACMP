t = [*map(int, open(0).read().split())]
n = t[0]
R = []
for i in range(n):
    x, y, u, v, r = t[1 + 5 * i:6 + 5 * i]
    R.append((min(x, u) - r, max(x, u) + r, min(y, v) - r, max(y, v) + r))
p = [*range(n)]
f = lambda x: x if p[x] == x else f(p[x])
for i in range(n):
    for j in range(i):
        a, b = R[i], R[j]
        if a[0] <= b[1] and b[0] <= a[1] and a[2] <= b[3] and b[2] <= a[3]:
            p[f(i)] = f(j)
print(sum(p[i] == i for i in range(n)))