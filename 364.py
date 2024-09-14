n, m = map(int, input().split())
a = [0]*10
a[1] = 6
a[2] = 28
a[3] = 496
a[4] = 8128
a[5] = 33550336
a[6] = 8589869056
a[7] = 137438691328
a[8] = 2305843008139952128
a[9] = 2658455991569831744654692615953842176
f = False
for i in a:
    if (i >= n) and (i <= m):
        print(i)
        f = True
if not f:
    print("Absent")