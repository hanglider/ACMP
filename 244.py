n, k, *a = map(int, open(0).read().split())
b = [i for i in range(k) if len(set(a[i::k])) > 1]
t = [0] * (not b)
if len(b) == 1:
    i = b[0]
    c = a[i::k]
    t = [i + c.index(v) * k + 1 for v in (0, 1) if c.count(v) == 1]
print(*["OK", min(t)] if t else ["FAIL"], sep="\n")
