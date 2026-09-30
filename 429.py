_, *s = open(0)
c = {}
v = {}
for i, l in enumerate(s, 2):
    a = l.split()
    c.setdefault(int(a[1]), []).append(i)
    if a[0] == 'L':
        v[i] = int(a[2])
q = [1]
d = {1: 1}
for x in q:
    for y in c.get(x, []):
        d[y] = -d[x]
        q += [y]
for x in q[::-1]:
    if x in c:
        v[x] = d[x] * max(d[x] * v[y] for y in c[x])
print(['0', '+1', '-1'][v[1]])
