n, m, *g = open(0).read().split()
r = [i for i, x in enumerate(g) if "*" in x] or [200]
c = [j for j, x in enumerate(zip(*g)) if "*" in x]
for i, x in enumerate(g):
    print("".join(".*"[r[0] <= i <= r[-1] and c[0] <= j <= c[-1]] for j in range(len(x))))
