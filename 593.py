from itertools import accumulate, repeat
from operator import sub, truediv, le, gt
from itertools import compress
from bisect import bisect_left
n, *v = map(int, open(0).read().split())
p = sorted(zip(map(float, v[::2]), map(float, v[1::2]), range(n)))
x, h, k = zip(*p)
s = list(accumulate(h[::-1], max))[::-1]
r = [0] * n
t = 0
for i in range(n):
    j = i + 1
    b = 32
    m = -1e9
    z = bytearray(2 * n)
    while j < n:
        e = min(j + b, n)
        if m > 0 and h[i] + m * (x[j] - x[i]) > s[j] + 1:
            break
        if h[i] + m * (x[j if m > 0 else e - 1] - x[i]) < max(h[j:e]) + 1:
            a = list(map(truediv, map(sub, h[j:e], repeat(h[i])), map(sub, x[j:e], repeat(x[i]))))
            c = max(a)
            if c >= m:
                d = []
                if a[-1] == c and a != sorted(a):
                    d = list(compress(range(1, e - j), map(gt, a, a[1:])))
                if a[-1] == c and len(d) * 8 < e - j:
                    u = 0
                    for w in d + [e - j]:
                        f = bisect_left(a, m, u, w)
                        z[2 * (j + f):2 * (j + w):2] = b'\1' * (w - f)
                        m = max(m, a[w - 1])
                        u = w
                else:
                    z[2 * j:2 * e:2] = bytes(map(le, accumulate(a, max, initial=m), a))
                m = c
        j = e
        b *= 2
    r[k[i]] = z.count(1)
    t += int.from_bytes(z, 'little')
for i, c in enumerate(memoryview(t.to_bytes(2 * n, 'little')).cast('H')):
    r[k[i]] += c
print(*r, sep='\n')
