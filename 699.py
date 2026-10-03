k, t, *a = map(int, open(0).read().split())
for i in range(0, 3 * k, 3):
    for j in range(i + 3, 3 * k, 3):
        t = min(t, ((a[i] - a[j])**2 + (a[i + 1] - a[j + 1])**2)**.5 / 2 - (a[i + 2] + a[j + 2]) / 2)
print('%.2f' % max(t, 0))
