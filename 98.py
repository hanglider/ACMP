a = [*map(int, open(0).read().split()[1:])]
r = []
while a:
    r += a.pop(-(a[0] < a[-1])),
print(sum(r[::2]), sum(r[1::2]), sep=':')