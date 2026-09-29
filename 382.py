n, *s = open(0).read().split()
w = int(n) + 1
g = " ".join(s) + " " * w
q = [0, len(g) - w - 1]
p = {*q}
c = -4
for i in q:
    for j in i - 1, i + 1, i - w, i + w:
        if g[j] != ".":
            c += 1
        elif j not in p:
            p |= {j}
            q += [j]
print(c * 25)
