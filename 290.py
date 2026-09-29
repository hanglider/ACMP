a = open(0).read().split()
n = int(a[0])
f = lambda s: int(s.translate({46: 48, 35: 49}), 2)
p = [*map(f, a[2:n + 2])]
d = [*map(f, a[n + 4:])]
print(sum(all(d[i + j] >> s & q == q for j, q in enumerate(p)) for i in range(len(d) - n + 1) for s in range(int(a[n + 3]) - int(a[1]) + 1)))
