b = [x.split() for x in open(0).read().split("*****")][:-1]
b[0].pop(0)
p = [x[0] for x in b]
r = [sum(1 << p.index(y) for y in x[2:]) for x in b]
n = len(p)
for k in range(n):
    for i in range(n):
        if r[i] >> k & 1:
            r[i] |= r[k]
for i in range(n):
    print("YNEOS"[r[i] >> i & 1 ^ 1::2])
