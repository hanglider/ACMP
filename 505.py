f = open(0)
l, m, n = map(int, f.readline().split())
d = {}
for _ in range(m):
    a, *s = f.readline().split()
    d[hash(tuple(s))] = a
k = 0
for _ in range(n):
    r = d.get(hash(tuple(f.readline().split())), '-')
    k += r > '-'
    print(r)
print(f'OK={k} BAD={n - k}')
