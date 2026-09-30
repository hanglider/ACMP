m = list(map(int, open(0).read().split()))
s = set()
for i in range(1, len(m), 6):
    a, b, c, d, e, f = m[i:i + 6]
    x = (c - a) * (f - b) - (d - b) * (e - a)
    t = ((a - c)**2 + (b - d)**2, (c - e)**2 + (d - f)**2, (e - a)**2 + (f - b)**2)
    if x < 0:
        t = t[::-1]
    s.add(min(u[j:] + u[:j] for u in [t, t[::-1]][:1 + (x == 0)] for j in range(3)))
print(['NO', 'YES'][len(s) < 2])
