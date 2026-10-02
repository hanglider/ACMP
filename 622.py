n, *a = map(int, open(0).read().split())
X = sorted(set(a[::2]))
Y = sorted(set(a[1::2]))
H = len(Y) + 2
W = len(X) + 2
b = set()
d = set()
for k in range(0, 4 * n, 4):
    x, z = sorted([X.index(a[k]) + 1, X.index(a[k + 2]) + 1])
    y, t = sorted([Y.index(a[k + 1]) + 1, Y.index(a[k + 3]) + 1])
    for j in range(y + 1, t + 1):
        b |= {x * H + j, z * H + j}
    for i in range(x + 1, z + 1):
        d |= {i * H + y, i * H + t}
s = bytearray(W * H) + b'\1' * H
r = 0
for c in range(W * H):
    if not s[c]:
        r += 1
        s[c] = 1
        o = [c]
        while o:
            c = o.pop()
            for e, f in (c + H, c not in b), (c - H, c - H not in b), (c + 1, c not in d), (c - 1, c - 1 not in d):
                if f and not s[e]:
                    s[e] = 1
                    o.append(e)
print(r)
