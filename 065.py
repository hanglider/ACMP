s, _, *m = open(0).read().split()
d = [sum(x != y for x, y in zip(s, t)) for t in m]
v = min(d, default=0)
r = [i + 1 for i, x in enumerate(d) if x == v]
print(len(r))
print(*r)
