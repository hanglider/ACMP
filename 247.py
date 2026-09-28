n, *a = map(int, open(0).read().split())
i = 9**9
d = [[0] + [i] * (n + 1)]
for x in a:
    p = d[-1]
    d += [[min(p[j - (x > 100)] + x, p[j + 1]) for j in range(n + 1)] + [i]]
m = min(d[-1])
k = r = n - d[-1][n::-1].index(m)
u = 0
for t in range(n, 0, -1):
    if d[t][k] == d[t - 1][k + 1]:
        u += 1
        k += 1
    else:
        k -= a[t - 1] > 100
print(m)
print(r, u)
