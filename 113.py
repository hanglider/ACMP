n, *g = open(0).read().split()
m = [int(x, 2) for x in g]
s = 0
while any(m):
    s += 1
    m = [a & b & (a & b) >> 1 for a, b in zip(m, m[1:])]
print(s * s)
