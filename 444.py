n, *a = map(int, open(0).read().split())
a = sorted(set(a))
d = [(0, '')]
r = 0
for i in range(len(a)):
    if a[i] - a[i - 1] != 1:
        r = i
    c, j, s = min((d[j][0] + len(s) + 2, j, s) for j in range(r, i + 1) for s in [[f'{a[j]}, ..., {a[i]}', str(a[i])][j == i]])
    d += [(c, d[j][1] + ', ' + s)]
print(d[-1][1][2:])
