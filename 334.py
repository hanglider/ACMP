from bisect import *
n, *a = map(int, open(0).read().replace(":", " ").split())
k = iter(a)
a = sorted(h % 12 * 3600 + m * 60 + s for h, m, s in zip(k, k, k))
t = min(a, key=lambda t: (n * t - 43200 * bisect(a, t), t < 3600))
print("%d:%02d:%02d" % (t // 3600 or 12, t // 60 % 60, t % 60))
