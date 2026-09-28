n, m, *a = map(int, open(0).read().split())
k = m + 1
g = [10**5] * k
for i in range(n):
    g += a[i * m:i * m + m] + [10**5]
g += [10**5] * k
v = set()
r = 0
for i in range(len(g)):
    if g[i] < 10**5 and i not in v:
        v.add(i)
        f = [i]
        c = 1
        for j in f:
            for x in j - 1, j + 1, j - k, j + k:
                c &= g[x] >= g[i]
                if g[x] == g[i] and x not in v:
                    v.add(x)
                    f += x,
        r += c
print(r)
