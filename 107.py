s = input()
d = dict(zip("00 010 002 011 000 0102 0121 0101 0022 0110 0111 0100 0010 0003 0000".split(), map(int, "222232233433335")))
r = []
for m in range(64):
    t = "".join(c + "-" * (m >> i & 1) for i, c in enumerate(s))
    g = t.split("-")
    if all(1 < len(x) < 5 for x in g):
        r += [(sum(d.get("".join(map(str, map(x.index, x))), 0) for x in g), t)]
v, t = max(r)
print(t)
print(v)
