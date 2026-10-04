f = open(0)
f.readline()
c = [0] * 6001
s = 0
for l in f:
    a, b = map(int, l.split())
    c[a + b] += 1
    s += b
d = []
for v in range(6001):
    d += [v] * c[v]
print(sum(d[::-2]) - s)
