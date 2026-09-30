from collections import Counter
n, m = map(int, input().split())
g = ''.join(input().ljust(m)[:m] for _ in range(n))
c = [10**9 if x == '@' else 0 for x in g]
e = n * m - m - 2
p = m + 1
s = {p}
L = [p]
for x in L:
    for y in x + 1, x - 1, x + m, x - m:
        if g[y] < '@' and y not in s:
            s.add(y)
            L.append(y)


def f(c, m, e, p):
    d = m
    c[p] = 1
    L = [p]
    h = {}
    l = {}
    l2 = {}
    O = m, 1, -m, -1
    while p != e:
        a = c[p + m]
        b = c[p + 1]
        u = c[p - m]
        v = c[p - 1]
        t = min(a, b, u, v)
        if c[p + d] != t:
            d = m if a == t else 1 if b == t else -m if u == t else -1
        p += d
        c[p] += 1
        L.append(p)
        s = p * 512 + d
        i = len(L) - 1
        j = h.get(s, -1)
        h[s] = i
        if i - j == l.get(s) == l2.get(s):
            k = 10**9
            C = Counter(L[j + 1:])
            z = Counter()
            for t in range(i - 1, j - 1, -1):
                y = L[t + 1]
                z[y] += 1
                r = c[y] - z[y]
                x = C[y]
                for o in O:
                    q = L[t] + o
                    w = x - C[q]
                    if w:
                        u = r - c[q] + z[q]
                        if u * w <= 0:
                            k = min(k, (abs(u) - 1) // abs(w))
                if k < 1:
                    break
            if 0 < k < 10**9:
                for q in C:
                    c[q] += k * C[q]
                L = [p]
                h = {s: 0}
                l = {}
                l2 = {}
                continue
        l2[s] = l.get(s)
        l[s] = i - j
    return sum(x for x in c if x < 10**9) - 1


print(f(c, m, e, p) if e in s else -1)
