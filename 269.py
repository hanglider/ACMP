a = open("input.txt").read().split()
x, y = a[0], a[1]
la, lb = len(x), len(y)
best = 0
for s in range(-(lb - 1), la):
    ov = 0
    ok = True
    for i in range(la):
        j = i - s
        if 0 <= j < lb:
            ov += 1
            if x[i] == '2' and y[j] == '2':
                ok = False
                break
    if ok and ov > best:
        best = ov
print(la + lb - best)
