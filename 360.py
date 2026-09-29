from array import array
f = open(0)
n = int(f.readline())
S = int('80000000' * n, 16)
C = int('7ffffc18' * n, 16)
g = lambda a, b: a & (F := (x := (a | S) - b & S) - (x >> 31)) | b & ~F
r = lambda: (l := f.readline().split()) and (int.from_bytes(array('i', map(int, l)), 'little') ^ S) - C or 0
p = m = 0
c = r()
for i in range(n):
    q = r()
    a = c << 32
    b = c >> 32
    m = g(m, g(g(p + q, a + b), g(p, q) + g(a, b)) + c)
    p = c
    c = q
print(max(array('i', m.to_bytes(4 * n + 4, 'little'))) - 3000)
