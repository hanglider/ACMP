n, m = map(int, input().split())
g = [input() for _ in range(n)]
w = lambda r, c: not (0 <= r < n and 0 <= c < m) or g[r][c] == '*'
k = [[0] * m for _ in g]
s = [(r, g[r].find('X'), a, b) for r in range(n) if 'X' in g[r] for a in (1, -1) for b in (1, -1)]
v = set()
while s:
    t = s.pop()
    if t in v:
        continue
    v.add(t)
    r, c, a, b = t
    k[r][c] |= 1 + (a == b)
    x = w(r + a, c)
    y = w(r, c + b)
    if w(r + a, c + b):
        t = (r, c + b, -a, b) if x > y else (r + a, c, a, -b) if y > x else (r, c, -a, -b)
    else:
        t = (r, c, -a, -b) if x * y else (r + a, c + b, a, b)
    s += [t]
for r in range(n):
    print(''.join('*' if g[r][c] == '*' else './\\X'[k[r][c]] for c in range(m)))
