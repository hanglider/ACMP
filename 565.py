import sys
f = open(0, 'rb')
n, r = map(int, f.readline().split())
k = r - 1 or 1
a = []
i = 1
for c in iter(lambda: f.readlines(2**16), []):
    v = list(map(int, b''.join(c).split()))
    a += [d << 48 | (w - d - 1) // k + 1 << 17 | j for w, d, j in zip(v[::2], v[1::2], range(i, n + 1)) if w > d]
    i += len(c)
a.sort()
s = 0
for v in a:
    s += v >> 17 & 2**31 - 1
    if s > v >> 48 or r < 2:
        exit(print("Impossible"))
s = 0
for v in a:
    sys.stdout.write('%d %d\n' % (s, v % 2**17))
    s += v >> 17 & 2**31 - 1
