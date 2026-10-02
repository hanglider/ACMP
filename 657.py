from sys import stdin
from itertools import *
for _ in range(int(next(stdin))):
    t = list(map(int, islice(stdin, int(next(stdin)))))
    x = t[0]
    c = [1 + (220 * y < 180 * x or 180 * y > 220 * x) for y in t]
    s = ''.join(map(str.__mul__, cycle('10'), c))
    a = s[::2]
    l = max(map(int.__floordiv__, [180 * y for y in t], c))
    h = min(map(int.__floordiv__, [220 * y for y in t], c))
    print(a if l <= h and len(s) % 2 < 1 and a.translate({48: 49, 49: 48}) == s[1::2] else 'ERROR')
