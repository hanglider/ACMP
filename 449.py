d = open('input.txt').read().split()
l = int(d[0])
x = sorted(map(int, d[2:]))
c, lim = 0, -1e9
for v in x:
    if v > lim:
        c += 1
        lim = v + 2 * l
print(c)
