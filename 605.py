from itertools import product
n = int(input())
d = []
for i in range(1, 21):
    d += [(str(i), i), ('D%d' % i, 2 * i), ('T%d' % i, 3 * i)]
d += [('25', 25), ('Bull', 50)]
r = sorted(p + (j,) for k in (0, 1, 2) for p in product(range(62), repeat=k) for j in [*range(1, 60, 3), 61] if sum(d[i][1] for i in p) + d[j][1] == n)
print(len(r))
for p in r:
    print(*(d[i][0] for i in p))
