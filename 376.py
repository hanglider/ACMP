from datetime import date
d, m, a, b, y = map(int, open(0).read().split())
c = date(y, b, a)
while 1:
    try:
        t = date(y, m, d)
        if t >= c:
            break
    except ValueError:
        pass
    y += 1
print((t - c).days)
