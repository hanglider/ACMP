n, m, k, *a = map(int, open(0).read().split())
g = {}
for i in range(0, 3 * m, 3):
    u, v, c = a[i:i + 3]
    g.setdefault((c, u), set()).add(v)
s = {a[-1]}
for c in a[3 * m + 1:-1]:
    s = set().union(*(g.get((c, u), ()) for u in s))
if s:
    print("OK")
    print(len(s))
    print(*sorted(s))
else:
    print("Hangs")
