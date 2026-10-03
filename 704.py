from math import *
n, m, *a = map(int, open(0).read().split())
p = [(2 * x - n, 2 * y - n) for x, y in zip(a[::2], a[1::2])]
t = sorted(atan2(y, x) for x, y in p)
t += [t[0] + 2 * pi]
print("YES" if (0, 0) not in p and max(t[i + 1] - t[i] for i in range(m)) > pi + 1e-9 else "NO")
