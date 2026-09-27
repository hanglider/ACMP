n, *a = map(int, open(0).read().split())
q = [0]
for u in q:
    q += [v for v in range(n) if a[u * n + v] and v not in q]
print("YNEOS"[sum(a) != 2 * n - 2 or len(q) < n::2])
