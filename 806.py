from itertools import accumulate as c
n, *a = map(int, open(0).read().split())
p = sorted(range(n), key=lambda i: -a[i] - a[n + i])
t = [0, *c(a[i] for i in p)]
print(*(i + 1 for i in p) if min(t[j] + a[i] + a[n + i] for j, i in enumerate(p)) > t[n] else [-1])
