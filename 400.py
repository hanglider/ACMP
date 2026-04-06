a = []
for _ in range(6):
    w, h = map(int, input().split())
    if w > h:
        w, h = h, w
    a.append((w, h))

a.sort()

ok = True
ok &= a[0] == a[1]
ok &= a[2] == a[3]
ok &= a[4] == a[5]
ok &= a[0][0] == a[2][0]
ok &= a[0][1] == a[4][0]
ok &= a[2][1] == a[4][1]

print("POSSIBLE" if ok else "IMPOSSIBLE")