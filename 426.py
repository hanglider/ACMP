n, *r = open(0).read().split()
w = int(n) + 1
g = list("#" * w + "#".join(r) + "#" * w * 2)
s = g.index("@")
e = g.index("X")
p = {s: s}
q = [s]
for v in q:
    for u in v - 1, v + 1, v - w, v + w:
        if g[u] in ".X" and u not in p:
            p[u] = v
            q += u,
print("NY"[e in p])
if e in p:
    while e != s:
        g[e] = "+"
        e = p[e]
    print("".join(g[w:-2 * w]).replace("#", "\n"))
