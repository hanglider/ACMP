from itertools import combinations as c
n, *a = map(int, open(0).read().split())
m = max((((x + y + z) * (x + y - z) * (x - y + z) * (y + z - x), i, j, k) for (i, x), (j, y), (k, z) in c(enumerate(a, 1), 3)), default=(0,))
if m[0] < 1:
    print(-1)
else:
    print(m[0]**.5 / 4)
    print(*m[1:])
