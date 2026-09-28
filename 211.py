w, h, *s = open(0).read().split()
m = int(w) + 3
g = 'X' * m + ''.join(x + 'X' for x in ['.' * (m - 1)] + ['.' + x + '.' for x in s[:int(h)]] + ['.' * (m - 1)]) + 'X' * m
q = list(map(int, s[int(h):]))
for i in range(0, len(q) - 4, 4):
    a, b, c, e = q[i:i + 4]
    t = m + e * m + c
    d = {m + b * m + a: 0}
    f = list(d)
    for j in f:
        for k in j - 1, j + 1, j - m, j + m:
            if (g[k] == '.' or k == t) and k not in d:
                d[k] = d[j] + 1
                f += k,
    print(d.get(t, 0))
