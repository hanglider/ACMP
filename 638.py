n, k, w, e, s, *d = map(int, open(0).read().split())
b = {*d[:e]}
h = {*d[e + 1:]}
r = c = 0
for i in range(n):
    c = (c + 1) * ((s + i - 1) % w + 1 not in b and i + 1 not in h)
    r += c >= k
print(r)
