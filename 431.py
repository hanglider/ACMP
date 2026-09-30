n, *s = open(0).read().split()
n = int(n)
w = n + 2
g = list('#' * w * 2 + ''.join(r + '##' for r in s) + '#' * w * 2)
a, b = [i for i, x in enumerate(g) if x == '@']
p = {a: a}
q = [a]
for x in q:
    for d in 2 * w - 1, 2 * w + 1, w - 2, w + 2:
        for y in x + d, x - d:
            if g[y] != '#' and y not in p:
                p[y] = x
                q += [y]
if b in p:
    x = p[b]
    while x != a:
        g[x] = '@'
        x = p[x]
    t = ''.join(g)
    for i in range(n):
        print(t[(i + 2) * w:][:n])
else:
    print('Impossible')
