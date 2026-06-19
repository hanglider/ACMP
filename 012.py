def inside(px, py, pts):
    sign = 0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
        if cross != 0:
            s = 1 if cross > 0 else -1
            if sign == 0:
                sign = s
            elif sign != s:
                return False
    return True

n = int(input())
cnt = 0
for _ in range(n):
    a = list(map(int, input().split()))
    x, y = a[0], a[1]
    pts = [(a[2], a[3]), (a[4], a[5]), (a[6], a[7]), (a[8], a[9])]
    if inside(x, y, pts):
        cnt += 1
print(cnt)
