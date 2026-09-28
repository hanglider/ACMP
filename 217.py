m, *a = map(int, open(0).read().split())
p = list(zip(a[:2 * m:2], a[1:2 * m:2]))
x = a[2 * m + 1:]
d = []
for i in range(len(x)):
    g = [max([v for v, (w, e) in zip(d[j], p) if e <= x[i] - x[j]] + [0]) for j in range(i)]
    d.append([1 + max([g[j] for j in range(i) if x[i] - x[j] >= w] + [0]) for w, e in p])
print(max(map(max, d)))
