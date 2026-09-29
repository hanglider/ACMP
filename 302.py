n, *a = open(0).read().split()
r = [complex(float(x), float(y)) for x, y in zip(a[::2], a[1::2])]
p = r.pop()
d = [abs(p - q) for q in r]
m = 0
while d:
    i = d.index(min(d))
    m = max(m, d.pop(i))
    p = r.pop(i)
    d = list(map(min, d, map(abs, map(p.__rsub__, r))))
print('%.2f' % m)
