k = int(input())
b = 0
for s in range(14):
    c = r = 0
    for d in range(1, 366):
        h = d <= k or d in (54, 67 + s // 7)
        w = (d + s) % 7 < 2
        c += h * w
        o = h or w or c > 0
        c -= o > h + w
        r = (r + 1) * o
        b = max(b, r)
print(b)
