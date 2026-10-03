from heapq import merge
from array import array
d = list(map(int, open(0).read().split()))
k = d[2]
A = [d[3 + 4 * i:7 + 4 * i] for i in range(k)]
p = 3 + 4 * k
n = d[p]
B = [d[p + 1 + 4 * i:p + 5 + 4 * i] for i in range(n)]
a, b, c, q = zip(*A)
e, h, v, g = zip(*B)
if (n * sum(c) - n * sum(a) + k * sum(v) - k * sum(e)) * (max(b) - min(b) + max(g) - min(g) + 1) < (n * sum(q) - n * sum(b) + k * sum(g) - k * sum(h)) * (max(a) - min(a) + max(v) - min(v) + 1):
    A = [[b, a, q, c] for a, b, c, q in A]
    B = [[h, e, g, v] for e, h, v, g in B]
o = 1 << 32
u = sorted(((o + 1 - 2 * g) << 18) + j for j, (e, h, v, g) in enumerate(B))
w = sorted(((o - 2 * h) << 18) + j for j, (e, h, v, g) in enumerate(B))
L = array('i', [0]) * (k * n)
R = array('i', L)
y = 0
t = 0
for x in merge(*[map(((2 * b << 18) + i * n).__add__, u) for i, (a, b, c, q) in enumerate(A)], *[map(((2 * q << 18) + i * n).__add__, w) for i, (a, b, c, q) in enumerate(A)]):
    j = x & 262143
    if x >> 18 & 1:
        t = 1
        L[j] = y
    else:
        y += t
        t = 0
        R[j] = y
u = sorted(((o + 1 - 2 * v) << 18) + j for j, (e, h, v, g) in enumerate(B))
w = sorted(((o - 2 * e) << 18) + j for j, (e, h, v, g) in enumerate(B))
I = bytes(range(1, 256)) + b'\0'
D = b'\xff' + bytes(range(255))
z = bytearray(y)
H = array('i', [0]) * y
m = 0
for x in merge(*[map(((2 * a << 18) + i * n).__add__, u) for i, (a, b, c, q) in enumerate(A)], *[map(((2 * c << 18) + i * n).__add__, w) for i, (a, b, c, q) in enumerate(A)]):
    j = x & 262143
    l = L[j]
    r = R[j]
    if x >> 18 & 1:
        s = z[l:r].translate(I)
        z[l:r] = s
        if m < 255:
            m += m + 1 in s
            continue
        i = s.find(0)
        while i >= 0:
            H[l + i] += 1
            i = s.find(0, i + 1)
        t = m + 1
        i = s.find(t & 255)
        while i >= 0:
            if H[l + i] == t >> 8:
                m = t
                break
            i = s.find(t & 255, i + 1)
    else:
        s = z[l:r].translate(D)
        z[l:r] = s
        if m > 255:
            i = s.find(255)
            while i >= 0:
                H[l + i] -= 1
                i = s.find(255, i + 1)
print(m)
