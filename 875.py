n, m, k, *t = open(0).read().split()
m = int(m)
N = int(n) * m
F = (1 << N) - 1
L = F // ((1 << m) - 1)
Z = L << m - 1
g = int(''.join(t).translate({42: 49, 46: 48}), 2)
for _ in range(int(k)):
    a = g << 1 & F - L | g >> m - 1 & L
    b = g >> 1 & F - Z | g << m - 1 & Z
    p = q = r = 0
    for y in g, a, b:
        for x in y, y >> m | y << N - m & F, y << m & F | y >> N - m:
            c = p & x
            p ^= x
            d = q & c
            q ^= c
            r ^= d
    g = p & q & ~r | g & r & ~(p | q)
s = f'{g:0{N}b}'.translate({48: 46, 49: 42})
for i in range(0, N, m):
    print(s[i:i + m])
