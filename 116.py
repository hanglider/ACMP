n, m, *g = open(0).read().split()
m = int(m) + 1
y = int("0".join(g), 2)
b = z = h = 0
w = m
while y:
    h += 1
    if z < 1 and b // h < w:
        p = [y]
        for j in range(9):
            p += [p[j] & p[j] >> 2**j]
        z = -1
        w = 0
        for j in range(9, -1, -1):
            t = z & p[j] >> w
            if t:
                z = t
                w += 2**j
    if z:
        b = max(b, h * w)
    y &= y >> m
    z &= z >> m
print(b)
