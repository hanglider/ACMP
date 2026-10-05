from math import gcd


def separate(seg1, seg2):
    (ax, ay), (bx, by) = seg1
    (cx, cy), (dx, dy) = seg2
    candidates = [
        (by - ay, ax - bx), (dy - cy, cx - dx),
        (bx - ax, by - ay), (dx - cx, dy - cy),
        (ax - cx, ay - cy), (ax - dx, ay - dy),
        (bx - cx, by - cy), (bx - dx, by - dy),
    ]
    for nx, ny in candidates:
        if nx == 0 and ny == 0:
            continue
        p1 = [nx * x + ny * y for x, y in seg1]
        p2 = [nx * x + ny * y for x, y in seg2]
        if max(p1) < min(p2):
            low, high = max(p1), min(p2)
        elif max(p2) < min(p1):
            low, high = max(p2), min(p1)
        else:
            continue
        a, b, c = 2 * nx, 2 * ny, -(low + high)
        g = gcd(gcd(a, b), c)
        return a // g, b // g, c // g
    return None


data = list(map(int, open("INPUT.TXT").read().split()))
out = []
pos = 0
while pos + 8 <= len(data):
    v = data[pos:pos + 8]
    pos += 8
    if all(x == 0 for x in v):
        break
    seg1 = [(v[0], v[1]), (v[2], v[3])]
    seg2 = [(v[4], v[5]), (v[6], v[7])]
    a, b, c = separate(seg1, seg2)
    out.append("%d %d %d" % (a, b, c))
open("OUTPUT.TXT", "w").write("\n".join(out) + "\n")
