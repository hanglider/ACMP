from array import array
from itertools import accumulate as A
from operator import sub
n, w, l, r, R, *a = map(int, open(0).read().split())
c = [0, *A(a)]
I = 2**29
W = R - r + 1
p = 32 * (w + R)
k = lambda v: int.from_bytes(array('I', v), 'little')
t = k([I] * w + list(map(sub, c[w:], c)))
h = k([2**31] * (l + 2 * w + 2 * R))
f = k([0] + [I] * l)
for _ in range(n):
    x = f << p | k([I] * (w + R))
    s = 1
    while 2 * s <= W:
        y = x >> 32 * s
        g = ((x | h) - y) & h
        x ^= (x ^ y) & g - (g >> 31)
        s *= 2
    y = x >> 32 * (W - s)
    g = ((x | h) - y) & h
    x ^= (x ^ y) & g - (g >> 31)
    f = t + x & (1 << 32 * l + 32) - 1
v = array('I', f.to_bytes(4 * l + 4, 'little'))[max(0, l - R):l - r + 1]
m = min([*v, I])
print(m if m < I else "No solution.")
