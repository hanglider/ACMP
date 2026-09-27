n, s, *a = map(int, open(0).read().split())
q = [s - 1]
for u in q:
    q += [v for v in range(n) if a[u * n + v] and v not in q]
print(len(q) - 1)
