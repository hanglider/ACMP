n, m, *s = open(0).read().split()
n = int(n)
m = int(m)
r = [i for i in range(n) if '*' in s[i]]
f = 0
if r:
    a = r[0]
    b = r[-1]
    c = min(s[i].find('*') for i in r)
    e = max(s[i].rfind('*') for i in r)
    for k in range(3, 1001):
        for x in range(max(b - k, a - 1), min(a, b - k + 1) + 2):
            for y in range(max(e - k, c - 1), min(c, e - k + 1) + 2):
                f |= 0 <= x <= n - k and 0 <= y <= m - k and all('.' not in t[y + 1:y + k - 1] for t in s[x + 1:x + k - 1])
print(['CIRCLE', 'SQUARE'][f])
