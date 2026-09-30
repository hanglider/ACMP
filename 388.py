n, m, *d = map(int, open(0).read().split())
c = [max(d[j::m]) for j in range(m)]
print(sum(c.count(min(d[i:i + m])) for i in range(0, n * m, m)))
