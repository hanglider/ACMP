n, *s = open(0).read().split()
w = int(n) + 1
g = list(" ".join(s) + " " * w)
e = g.index("X")
a = g.index("@")
p = {e: e}
q = [e]
for i in q:
    for j in i - 1, i + 1, i - w, i + w:
        if j not in p and g[j] in ".@":
            p[j] = i
            q += [j]
if a in p:
    while a != e:
        a = p[a]
        g[a] = "+"
    print("Yes", *"".join(g).split(), sep="\n")
else:
    print("No")
