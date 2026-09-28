n, k, *d = open(0).read().split()
k = int(k)
t = 0
s = {}
e = {}
f = lambda x: '%02d:%02d:%02d' % (x // 3600 % 24, x // 60 % 60, x % 60)
for b in range(0, int(n), k):
    h, m, c = map(int, d[2 * b + 2 * k - 2].split(':'))
    t = max(t, h * 3600 + m * 60 + c)
    q = [(i, int(d[2 * i + 1])) for i in range(b, b + k)]
    while q:
        i, r = q.pop(0)
        s.setdefault(i, t)
        if r > 10:
            q += [(i, r - 10)]
            r = 10
        t += r
        e[i] = t
for i in s:
    print(f(s[i]), f(e[i]))
