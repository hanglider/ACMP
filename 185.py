n, k, *a = map(int, open(0).read().split())
e = [*zip(a[::2], a[1::2])]
q = [k]
for u in q:
    q += [y for x, y in e if x == u and y not in q]
print(["No", "Yes"][len(q) == n])
