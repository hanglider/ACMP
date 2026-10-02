from bisect import bisect_left as f
r = open(0)
r.readline()
b, e = map(int, r.readline().split())
x = [b]
y = [0]
for v in sorted(int(q) << 45 | int(p) << 15 | int(s) for p, q, s in map(str.split, r)):
    q = v >> 45
    i = f(x, v >> 15 & 2**30 - 1)
    if q > b and i < len(x):
        d = y[i] + v % 32768
        while y[-1] >= d:
            x.pop()
            y.pop()
        x.append(q)
        y.append(d)
print(y[f(x, e)])
