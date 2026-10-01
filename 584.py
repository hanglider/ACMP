m, n = map(int, input().split())
b = [m - 1, n - 1, 0, -2]
z = i = h = 0
p = [0]
s = []
while 1:
    d = 1j * (-1j)**(i % 4)
    l = b[i % 4] - (z / d).real
    if i and (l < 1 or h == 1):
        break
    h = i and l
    b[i % 4] -= 2
    if l:
        z += d * l
        p += [z]
        s += [d]
    i += 1
s = s or [1j]
o = [1 + 1j - s[0] * (1 - 1j)]
q = [1 + 1j - s[0] * (1 + 1j)]
for k in range(1, len(s)):
    c = 2 * p[k] + 1 + 1j
    e = (s[k - 1] + s[k]) * 1j
    o += [c + e]
    q += [c - e]
a = s[-1]
c = 2 * z + 1 + 1j + a
y = o + [c + a * 1j, c - a * 1j] + q[::-1]
k = y.index(0)
y = y[k:] + y[:k]
w = [B for A, B, C in zip(y[-1:] + y, y, y[1:] + y) if ((C - B) / (B - A)).imag]
w += w[:2]
r = []
for A, B, C in zip(w, w[1:], w[2:]):
    r += ['f %d' % (abs(B - A) / 2), 'lr'[((C - B) / (B - A)).imag < 0]]
print(len(r) - 1, *r[:-1], sep='\n')
