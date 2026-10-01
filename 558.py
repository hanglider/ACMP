n, *r = map(int, open(0).read().split())
r.sort()
m = len(r)
s = 0
for k in range(m):
    c = r[k]
    for d in r[:k]:
        def f(a, b):
            t = a * b * c - d * (a * b + b * c + c * a)
            return t >= 0 and 4 * d * d * a * b * c * (a + b + c) <= t * t
        if m - k < 3 or not f(r[-1], r[-2]):
            break
        i = m
        for j in range(k + 1, m):
            while i > j + 1 and f(r[i - 1], r[j]):
                i -= 1
            if i <= j + 1:
                q = m - j
                s += q * (q - 1) // 2
                break
            s += m - i
print(s)
