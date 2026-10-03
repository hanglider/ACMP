from operator import add
n, m, *t = map(int, open(0).read().split())
q = [-a for a in t[::2]]
d = [0] * 10**4
for x in range(10**4, 10**4 + n):
    d += [min(map(add, map(d.__getitem__, map(x.__add__, q)), t[1::2]))]
print(d[-1])
