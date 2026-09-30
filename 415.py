a, b = open(0).read().lower().split()
r = []
for x, y in (a, b), (b, a):
    for p in range(len(x) + 1):
        if x[p:].startswith(y) or y.startswith(x[p:]):
            t = max(x, x[:p] + y, key=len)
            t = t[:p] + t[p:].capitalize()
            t = t[0].upper() + t[1:]
            r += [(len(t), t)]
print(min(r)[1])
