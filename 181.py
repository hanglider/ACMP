l = open(0).read().splitlines()
d, m = l[6].split()
c = dict.fromkeys("NSWEUD", 1)
for _ in range(int(m) - 1):
    c = {x: 1 + sum(c[y] for y in r if y in c) for x, r in zip("NSWEUD", l)}
print(c[d])
