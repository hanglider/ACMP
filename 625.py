l = open(0).read().splitlines()
p = {}
for i in range(9):
    for j, c in enumerate(l[i]):
        p[c] = (i, j + 1)
r = 0
q = -1
x = 9**9
d = [x, x, 0]
for c in l[9]:
    if c == ' ':
        r += 1
        q = -1
        continue
    b, k = p[c.lower()]
    r += k + (b == q)
    q = b
    a = min(d[0], d[1] + 1, d[2] + 1)
    u = min(d[1], d[0] + 1, d[2] + 2)
    if c in '.?!':
        d = [x, u, min(a, d[2])]
    elif c.islower():
        d = [a, x, x]
    else:
        d = [d[2], u, x]
print(r + min(d))
