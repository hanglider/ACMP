r = open(0)
l = 1 << int(next(r))
a = list(map(int, next(r).split()))
next(r)
f = lambda k: (x := a[k] ^ a[k - 1]) & x - 1 > 0
b = sum(map(f, range(l)))
y = "Yes", "No"
o = []
for t in r:
    i, j = map(int, t.split())
    s = {i, j, -~i % l, -~j % l}
    b -= sum(map(f, s))
    a[i], a[j] = a[j], a[i]
    b += sum(map(f, s))
    o += [y[b > 0]]
print("\n".join(o))
