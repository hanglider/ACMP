m, n, k, *s = open(0).read().split()
n = int(n)
F = {(x + 1, y + 1) for y in range(n) for x in range(int(m)) if s[y][x] < 'X'}
D = {'U': (0, -1), 'L': (-1, 0), 'D': (0, 1), 'R': (1, 0)}
R = [(int(x), int(y), *D[z]) for x, y, z in zip(*[iter(s[n:])] * 3)]
t = 0
while R:
    t += 1
    R = [(x + a, y + b, a, b) for x, y, a, b in R if (x + a, y + b) in F]
    L = [q[:2] for q in R]
    R = [q for q in R if L.count(q[:2]) < 2]
    K = set()
    for x, y, a, b in R:
        x += a
        y += b
        while (x, y) in F:
            K |= {(x, y)}
            x += a
            y += b
    R = [q for q in R if q[:2] not in K]
print(t)
