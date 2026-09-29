from operator import add
n, k, *a = map(int, open(0).read().split())
w = n + 2
z = -10**9
v = [z] * w
for i in range(n):
    v += [z] + a[i * n:i * n + n] + [z]
v += [z] * w
b = [z] * w + list(map(max, v[w - 1:-w - 1], v[w + 1:-w + 1], v, v[2 * w:])) + [z] * w
u = list(map(add, b, v))
d = [z] * len(v)
d[w + 1] = v[w + 1]
r = 0
for t in range(min(k, 2 * n + 2)):
    s = k - 1 - t
    h = s // 2
    r = max(r, max(map(add, d, [x * h + y * (s % 2) for x, y in zip(u, b)])))
    d = [z] * w + list(map(add, map(max, d[w - 1:-w - 1], d[w + 1:-w + 1], d, d[2 * w:]), v[w:-w])) + [z] * w
print(r)
