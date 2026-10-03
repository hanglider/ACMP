n, m = map(int, open(0).read().split())
f = [1, 1]
for i in range(2000):
    f += [f[-1] + f[-2]]
print(2 * (f[n] + f[m] - 1))
