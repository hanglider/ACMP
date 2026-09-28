from itertools import accumulate as a
n, l, *s = map(int, open(0).read().split())
d = [0] + [9**9] * l
for p, r, q, f in zip(*[iter(s)] * 4):
    g = [*a([k * [q, p][k < r] for k in range(f, -1, -1)], min)][::-1]
    d = [min(map(int.__add__, d[t::-1], g)) for t in range(l + 1)]
print([d[l], -1][d[l] >= 9**9])
