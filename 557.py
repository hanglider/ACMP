import sys
L = sys.stdin
def R():
    s = L.readline()
    while s.strip() == '':
        s = L.readline()
    return s

m, n = map(int, R().split())
a, b = map(int, R().split())
p = int(R())
v = None
for t in range(m):
    rows = [list(map(int, R().split())) for _ in range(n)]
    if t == 0:
        v = rows[a - 1]
    else:
        w = [0] * n
        for r in range(n):
            x = v[r]
            if x:
                row = rows[r]
                for j in range(n):
                    w[j] += x * row[j]
        v = [x % p for x in w]
print(v[b - 1] % p)
