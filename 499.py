k, w, *t = map(int, open(0).read().split())
p = [(0, 0)]
for a, b in zip(t[::2], t[1::2]):
    p += [(x + a, y + b) for x, y in p]
print(['NO', 'YES'][any(x <= w and y >= k for x, y in p)])
