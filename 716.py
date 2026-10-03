n, p, *s = open(0).read().split()
l = 30
h = 4000
p = float(p)
for i in range(0, len(s), 2):
    f = float(s[i])
    m = (f + p) / 2
    if f != p:
        if (f > p) == (s[i + 1] < 'd'):
            l = max(l, m)
        else:
            h = min(h, m)
    p = f
print(l, h)
