s = set()
for x in open(0).read().split()[1:]:
    s ^= {int(x)}
l = [0, *sorted(s), 10**9]
print(max(y - x for x, y in zip(l[::2], l[1::2])))
