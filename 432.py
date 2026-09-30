s = {i + j * 1j for i, r in enumerate(open(0).read().split()[2:]) for j, c in enumerate(r) if c < "."}
k = 0
while s:
    q = [s.pop()]
    k += 1
    while q:
        p = q.pop()
        t = {p + 1, p - 1, p + 1j, p - 1j} & s
        s -= t
        q += t
print(k)
