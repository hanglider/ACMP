n, *s = map(int, open(0).read().split())
a = s.pop()
for x in sorted(s):
    a = max(a, (a + x) / 2)
print("%.6f" % a)
