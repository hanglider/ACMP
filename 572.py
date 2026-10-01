r = list(map(int, open(0).read().split()))
s = r[1]
f = [(r[2 * i + 2], r[2 * i + 3], i + 1) for i in range(r[0])]
o = []
for a, b, i in sorted(f):
    if b >= 0 <= s - a:
        s += b
        o += [i]
g = sorted((x for x in f if x[1] < 0), key=lambda x: -x[0] - x[1])
z = -9**9
d = [s]
t = []
for a, b, i in g:
    e = [z] + [x + b if x >= a else z for x in d]
    d += [z]
    t += [bytes(map(int.__gt__, e, d))]
    d = list(map(max, d, e))
k = len(d) - 1
while d[k] == z:
    k -= 1
q = []
for j in range(len(g) - 1, -1, -1):
    if t[j][k]:
        q += [g[j][2]]
        k -= 1
print(len(o) + len(q))
print(*o + q[::-1])
