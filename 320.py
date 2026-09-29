m, n = map(int, open(0).read().split())
f = [1] * m
for i in range(m, n + 1):
    f += [f[-1] + f[-m]]
print(f[n])
