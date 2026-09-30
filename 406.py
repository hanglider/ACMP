r = open(0).read().split()
n = int(r[0])
l = sorted(map(chr, range(97, 123)), key=r[-1].count)[26 - n:]
z = sorted(range(n), key=r[3::2].__getitem__)
print(*[l[z.index(i)] for i in range(n)], sep="\n")
