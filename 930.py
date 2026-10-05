x, y = open(0).read().split()
s = ''
for c in map(chr, range(122, 96, -1)):
    k = min(x.count(c), y.count(c))
    s += c * k
    x = x.split(c, k)[k]
    y = y.split(c, k)[k]
print(s)
