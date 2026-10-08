from array import array
n, *a = map(int, open(0).read().split())
m = [sum(a[i * n + j] << j for j in range(n)) | 1 << i for i in range(n)]
f = array("i", [1]) * (1 << n)
d = {1: (-1)**n}
for s in range(1, 1 << n):
    l = s & -s
    v = f[s] = f[s - l] + f[s & ~m[l.bit_length() - 1]]
    d[v] = d.get(v, 0) + (-1)**(n + bin(s).count("1"))
print(next(k for k in range(1, n + 1) if sum(c * v**k for v, c in d.items()) > 0))
