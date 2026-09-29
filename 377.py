n, *a = map(int, open(0).read().split())
s = 0
e = -3e9
for l, r in sorted(zip(a[::2], a[1::2])):
    s += max(0, r - max(l, e))
    e = max(e, r)
print(s)
