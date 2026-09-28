n, m, k, *a = map(int, open(0).read().split())
s = {*zip(a[::2], a[1::2])}
d = -1, 0, 1
for i in range(1, n + 1):
    print(''.join('*' if (i, j) in s else str(sum((i + x, j + y) in s for x in d for y in d) or '.') for j in range(1, m + 1)))
