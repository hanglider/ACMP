n, m, y, x = map(int, open(0).read().split())
v = set()
r = c = 0
a, b = 0, 1
k = 1
while (r, c) != (y - 1, x - 1):
    v.add((r, c))
    if not (0 <= r + a < n and 0 <= c + b < m) or (r + a, c + b) in v:
        a, b = b, -a
    r += a
    c += b
    k += 1
print(k)