n, *s = open(0).read().split()
a, b = map(int, s[-2:])
d = {}
for i in range(0, len(s) - 2, 4):
    x, y, r = map(int, s[i + 1:i + 4])
    d[s[i]] = d.get(s[i], 0) + ((x - a)**2 + (y - b)**2 <= r * r)
print(len(d))
for k in d:
    print(k, d[k])
