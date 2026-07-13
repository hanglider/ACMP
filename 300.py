from fractions import Fraction as F
d = list(map(int, open(0).read().split()))
p = d[8]
q = d[9]
a = sorted((d[2 * i] + F(q, d[2 * i + 1]), i) for i in range(4))
c = 0
w = 1
u = a[0][0]
s = a[0][1]
i = 0
while i < 4:
    j = i
    while j < 4 and a[j][0] == a[i][0]:
        j += 1
    t = a[i][0]
    if i == 0:
        c = 1
    else:
        h = 0
        for k in range(i, j):
            e = abs(a[k][1] - s) % 4
            e = min(e, 4 - e)
            if u + e * p <= t:
                h = 1
                s = a[k][1]
                break
        c += h
        if h == 0:
            w = 0
            break
    u = t
    if j - i > 1:
        w = 0
        break
    i = j
if w:
    print("ALIVE")
else:
    print(c)
