n, m, *s = open(0).read().split()
g = s[:int(n)]
x, y, l, *v = map(int, s[int(n):])
d = {(x, y): 0}
q = [(x, y)]
for x, y in q:
    for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if g[a - 1][b - 1] < '1' and (a, b) not in d:
            d[a, b] = d[x, y] + 1
            q += (a, b),
print(sum(v[i + 2] for i in range(0, 12, 3) if d.get((v[i], v[i + 1]), l + 1) <= l))
