from itertools import *
_, *t = map(int, open(0).read().split())
s = ''
for x, y, a in zip(*[iter(t)] * 3):
    s += str(+any((x - p - q) % a == (x - r - w) % a == (y - 2 + p + r) % a == (y - 2 + q + w) % a == 0 for p, q, r, w in product((0, 1), repeat=4)))
print(s)
