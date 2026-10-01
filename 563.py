from array import array
from functools import reduce
from itertools import accumulate, repeat
from operator import and_, xor
n, *a = map(int, open(0).read().split())
s = sorted(array('I', bytes(array('I', map(and_, a, repeat(2**32 - 1)))).translate(bytes(int(f'{i:08b}'[::-1], 2) for i in range(256)))[::-1]))
g = [*map(int.bit_length, map(xor, s, s[1:])), 98, 99]
c = [0] * 99
t = [-1]
for i, x in enumerate(g[:-1]):
    while g[t[-1]] <= x:
        j = t.pop()
        c[g[j]] ^= (j - t[-1]) * (i - j) & 1
    t += i,
r = 0
for x in accumulate(c[:32], xor):
    r = r * 2 + x
print(reduce(xor, a) ^ r - (r >> 31 << 32))
